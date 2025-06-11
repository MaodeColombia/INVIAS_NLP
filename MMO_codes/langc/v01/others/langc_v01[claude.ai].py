#!/usr/bin/env python3
"""
Sistema RAG (Retrieval-Augmented Generation) Mejorado para INVIAS
=================================================================

Sistema de consulta inteligente de documentos PDF usando LangChain y OpenAI.
Permite cargar documentos PDF, crear embeddings semánticos y responder preguntas
con trazabilidad de fuentes.

Autor: Mejorado por Claude
Versión: 2.0
"""

import os
import sys
import logging
import json
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
import traceback

# Librerías principales
import gradio as gr
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory


@dataclass
class Config:
    """Configuración del sistema RAG"""
    # Rutas
    pdf_directory: str = "../../../assets/DG_docs/PDF_test_gradio/"
    persist_directory: str = "chroma_db"
    log_file: str = "rag_system.log"
    config_file: str = "rag_config.json"
    
    # Parámetros de embeddings
    embedding_model: str = "text-embedding-3-small"  # Modelo más nuevo y eficiente
    chunk_size: int = 1500
    chunk_overlap: int = 200
    
    # Parámetros de LLM
    llm_model: str = "gpt-3.5-turbo"
    temperature: float = 0.0
    
    # Parámetros de recuperación
    retrieval_k: int = 5
    
    # Gradio
    server_name: str = "127.0.0.1"
    server_port: int = 7860
    share: bool = False


class Logger:
    """Sistema de logging mejorado"""
    
    def __init__(self, log_file: str = "rag_system.log"):
        self.setup_logging(log_file)
    
    def setup_logging(self, log_file: str):
        """Configura el sistema de logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file, encoding='utf-8'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def info(self, message: str):
        self.logger.info(message)
    
    def error(self, message: str, exc_info: bool = True):
        self.logger.error(message, exc_info=exc_info)
    
    def warning(self, message: str):
        self.logger.warning(message)


class DocumentProcessor:
    """Procesador de documentos PDF"""
    
    def __init__(self, config: Config, logger: Logger):
        self.config = config
        self.logger = logger
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.chunk_size,
            chunk_overlap=config.chunk_overlap,
            length_function=len
        )
    
    def load_pdfs(self) -> List[Any]:
        """Carga todos los PDFs de la carpeta especificada"""
        try:
            pdf_path = Path(self.config.pdf_directory)
            if not pdf_path.exists():
                raise FileNotFoundError(f"Directorio no encontrado: {pdf_path}")
            
            documents = []
            pdf_files = list(pdf_path.glob("*.pdf"))
            
            if not pdf_files:
                self.logger.warning(f"No se encontraron archivos PDF en {pdf_path}")
                return documents
            
            self.logger.info(f"📄 Cargando {len(pdf_files)} archivos PDF...")
            
            for pdf_file in pdf_files:
                try:
                    self.logger.info(f"Procesando: {pdf_file.name}")
                    loader = PyPDFLoader(str(pdf_file))
                    data = loader.load()
                    documents.extend(data)
                except Exception as e:
                    self.logger.error(f"Error cargando {pdf_file.name}: {str(e)}")
                    continue
            
            self.logger.info(f"✅ Total de páginas cargadas: {len(documents)}")
            return documents
            
        except Exception as e:
            self.logger.error(f"Error en load_pdfs: {str(e)}")
            return []
    
    def split_documents(self, documents: List[Any]) -> List[Any]:
        """Fragmenta los documentos en chunks más pequeños"""
        try:
            if not documents:
                self.logger.warning("No hay documentos para fragmentar")
                return []
            
            self.logger.info("🔪 Fragmentando documentos...")
            split_docs = self.text_splitter.split_documents(documents)
            self.logger.info(f"✅ Total de fragmentos creados: {len(split_docs)}")
            return split_docs
            
        except Exception as e:
            self.logger.error(f"Error fragmentando documentos: {str(e)}")
            return []


class VectorStoreManager:
    """Gestor de la base de datos vectorial"""
    
    def __init__(self, config: Config, logger: Logger):
        self.config = config
        self.logger = logger
        self.embeddings = None
        self.vectorstore = None
        self._initialize_embeddings()
    
    def _initialize_embeddings(self):
        """Inicializa el modelo de embeddings"""
        try:
            self.embeddings = OpenAIEmbeddings(model=self.config.embedding_model)
            self.logger.info(f"✅ Modelo de embeddings inicializado: {self.config.embedding_model}")
        except Exception as e:
            self.logger.error(f"Error inicializando embeddings: {str(e)}")
            raise
    
    def create_vectorstore(self, documents: List[Any]) -> bool:
        """Crea y persiste la base de datos vectorial"""
        try:
            if not documents:
                self.logger.error("No hay documentos para crear el vectorstore")
                return False
            
            self.logger.info("🔄 Creando base de datos vectorial...")
            
            # Crear vectorstore
            self.vectorstore = Chroma.from_documents(
                documents=documents,
                embedding=self.embeddings,
                persist_directory=self.config.persist_directory
            )
            
            # Persistir en disco
            self.vectorstore.persist()
            self.logger.info(f"✅ Base de datos guardada en: {self.config.persist_directory}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error creando vectorstore: {str(e)}")
            return False
    
    def load_vectorstore(self) -> bool:
        """Carga la base de datos vectorial existente"""
        try:
            persist_path = Path(self.config.persist_directory)
            if not persist_path.exists():
                self.logger.warning(f"Base de datos no encontrada en: {persist_path}")
                return False
            
            self.vectorstore = Chroma(
                embedding_function=self.embeddings,
                persist_directory=self.config.persist_directory
            )
            
            self.logger.info("✅ Base de datos vectorial cargada correctamente")
            return True
            
        except Exception as e:
            self.logger.error(f"Error cargando vectorstore: {str(e)}")
            return False
    
    def get_retriever(self):
        """Obtiene el retriever para búsqueda semántica"""
        if not self.vectorstore:
            raise ValueError("Vectorstore no inicializado")
        
        return self.vectorstore.as_retriever(
            search_kwargs={"k": self.config.retrieval_k}
        )


class RAGSystem:
    """Sistema RAG principal"""
    
    def __init__(self, config: Config):
        self.config = config
        self.logger = Logger(config.log_file)
        self.doc_processor = DocumentProcessor(config, self.logger)
        self.vector_manager = VectorStoreManager(config, self.logger)
        self.llm = None
        self.qa_chain = None
        self.conversational_chain = None
        self.memory = None
        self._initialize_llm()
    
    def _initialize_llm(self):
        """Inicializa el modelo de lenguaje"""
        try:
            api_key = os.environ.get("OPENAI_API_KEY")
            if not api_key:
                raise ValueError("Variable de entorno OPENAI_API_KEY no configurada")
            
            self.llm = ChatOpenAI(
                model=self.config.llm_model,
                temperature=self.config.temperature,
                api_key=api_key
            )
            
            self.logger.info(f"✅ LLM inicializado: {self.config.llm_model}")
        except Exception as e:
            self.logger.error(f"Error inicializando LLM: {str(e)}")
            raise
    
    def setup_system(self, force_rebuild: bool = False) -> bool:
        """Configura todo el sistema RAG"""
        try:
            self.logger.info("🚀 Iniciando configuración del sistema RAG...")
            
            # Intentar cargar vectorstore existente
            if not force_rebuild and self.vector_manager.load_vectorstore():
                self.logger.info("📁 Usando base de datos existente")
            else:
                self.logger.info("🔄 Creando nueva base de datos...")
                # Cargar y procesar documentos
                documents = self.doc_processor.load_pdfs()
                if not documents:
                    self.logger.error("No se pudieron cargar documentos")
                    return False
                
                # Fragmentar documentos
                split_docs = self.doc_processor.split_documents(documents)
                if not split_docs:
                    self.logger.error("No se pudieron fragmentar documentos")
                    return False
                
                # Crear vectorstore
                if not self.vector_manager.create_vectorstore(split_docs):
                    self.logger.error("No se pudo crear la base de datos vectorial")
                    return False
            
            # Configurar cadenas de QA
            self._setup_qa_chains()
            
            self.logger.info("✅ Sistema RAG configurado correctamente")
            return True
            
        except Exception as e:
            self.logger.error(f"Error configurando sistema: {str(e)}")
            return False
    
    def _setup_qa_chains(self):
        """Configura las cadenas de preguntas y respuestas"""
        try:
            retriever = self.vector_manager.get_retriever()
            
            # Cadena moderna con fuentes
            prompt = PromptTemplate.from_template(
                """Eres un asistente experto en documentos de INVIAS. 
                Usa los siguientes documentos para responder la pregunta de forma precisa y detallada.
                Si no encuentras información suficiente, indícalo claramente.
                
                Documentos de referencia:
                {context}
                
                Pregunta: {input}
                
                Respuesta:"""
            )
            
            combine_docs_chain = create_stuff_documents_chain(
                llm=self.llm,
                prompt=prompt
            )
            
            self.qa_chain = create_retrieval_chain(
                retriever=retriever,
                combine_docs_chain=combine_docs_chain
            )
            
            # Cadena conversacional con memoria
            self.memory = ConversationBufferMemory(
                memory_key="chat_history",
                return_messages=True
            )
            
            self.conversational_chain = ConversationalRetrievalChain.from_llm(
                llm=self.llm,
                retriever=retriever,
                memory=self.memory,
                return_source_documents=True
            )
            
            self.logger.info("✅ Cadenas de QA configuradas")
            
        except Exception as e:
            self.logger.error(f"Error configurando cadenas QA: {str(e)}")
            raise
    
    def ask_question(self, question: str, use_conversation: bool = False) -> Tuple[str, str]:
        """Responde una pregunta usando el sistema RAG"""
        try:
            if not question.strip():
                return "Por favor, ingresa una pregunta válida.", ""
            
            self.logger.info(f"❓ Pregunta recibida: {question}")
            
            if use_conversation and self.conversational_chain:
                # Usar cadena conversacional
                response = self.conversational_chain({"question": question})
                answer = response.get("answer", "No se pudo generar respuesta")
                sources = self._format_sources(response.get("source_documents", []))
            else:
                # Usar cadena estándar
                response = self.qa_chain.invoke({"input": question})
                answer = response.get("answer", "No se pudo generar respuesta")
                sources = self._format_sources(response.get("context", []))
            
            self.logger.info("✅ Respuesta generada correctamente")
            return answer, sources
            
        except Exception as e:
            error_msg = f"Error procesando pregunta: {str(e)}"
            self.logger.error(error_msg)
            return f"❌ {error_msg}", ""
    
    def _format_sources(self, source_docs: List[Any]) -> str:
        """Formatea las fuentes de información"""
        if not source_docs:
            return "No se encontraron fuentes específicas."
        
        formatted_sources = []
        for i, doc in enumerate(source_docs, 1):
            source_file = Path(doc.metadata.get("source", "desconocido")).name
            content_preview = doc.page_content[:300].replace("\n", " ").strip()
            formatted_sources.append(
                f"📄 Fuente {i}: {source_file}\n"
                f"Contenido: {content_preview}{'...' if len(doc.page_content) > 300 else ''}\n"
            )
        
        return "\n".join(formatted_sources)


class GradioInterface:
    """Interfaz de usuario con Gradio"""
    
    def __init__(self, rag_system: RAGSystem):
        self.rag_system = rag_system
        self.logger = rag_system.logger
    
    def create_interface(self):
        """Crea la interfaz de Gradio"""
        def process_question(question, use_conversation):
            try:
                answer, sources = self.rag_system.ask_question(question, use_conversation)
                return answer, sources
            except Exception as e:
                error_msg = f"Error en la interfaz: {str(e)}"
                self.logger.error(error_msg)
                return error_msg, ""
        
        # Crear interfaz
        with gr.Blocks(title="Sistema RAG - INVIAS", theme=gr.themes.Soft()) as interface:
            gr.HTML("<h1 style='text-align: center;'>🏗️ Sistema RAG para INVIAS</h1>")
            gr.HTML("<p style='text-align: center;'>Consulta inteligente de documentos PDF</p>")
            
            with gr.Row():
                with gr.Column(scale=2):
                    question_input = gr.Textbox(
                        label="💬 Tu pregunta",
                        placeholder="Ejemplo: ¿Qué es CCPT? ¿Qué acciones tomó INVIAS en Ocaña?",
                        lines=2
                    )
                    
                    with gr.Row():
                        submit_btn = gr.Button("🔍 Consultar", variant="primary")
                        clear_btn = gr.Button("🗑️ Limpiar")
                    
                    use_conversation = gr.Checkbox(
                        label="💭 Usar memoria conversacional",
                        value=False,
                        info="Mantiene el contexto de preguntas anteriores"
                    )
                
                with gr.Column(scale=1):
                    gr.HTML("""
                    <div style='padding: 20px; background-color: #f0f0f0; border-radius: 10px;'>
                        <h3>💡 Consejos de uso:</h3>
                        <ul>
                            <li>Haz preguntas específicas sobre los documentos</li>
                            <li>Usa la memoria conversacional para seguimiento</li>
                            <li>Revisa las fuentes para verificar información</li>
                        </ul>
                    </div>
                    """)
            
            with gr.Row():
                answer_output = gr.Textbox(
                    label="🧠 Respuesta",
                    lines=8,
                    max_lines=15
                )
                sources_output = gr.Textbox(
                    label="📚 Fuentes utilizadas",
                    lines=8,
                    max_lines=15
                )
            
            # Eventos
            submit_btn.click(
                fn=process_question,
                inputs=[question_input, use_conversation],
                outputs=[answer_output, sources_output]
            )
            
            clear_btn.click(
                fn=lambda: ("", "", ""),
                outputs=[question_input, answer_output, sources_output]
            )
        
        return interface
    
    def launch(self, config: Config):
        """Lanza la interfaz"""
        try:
            interface = self.create_interface()
            self.logger.info(f"🚀 Lanzando interfaz en {config.server_name}:{config.server_port}")
            
            interface.launch(
                server_name=config.server_name,
                server_port=config.server_port,
                share=config.share,
                show_error=True
            )
        except Exception as e:
            self.logger.error(f"Error lanzando interfaz: {str(e)}")


def main():
    """Función principal"""
    try:
        # Cargar configuración
        config = Config()
        
        # Crear sistema RAG
        rag_system = RAGSystem(config)
        
        # Configurar sistema
        if not rag_system.setup_system():
            print("❌ Error configurando el sistema RAG")
            return
        
        # Crear y lanzar interfaz
        gradio_interface = GradioInterface(rag_system)
        gradio_interface.launch(config)
        
    except KeyboardInterrupt:
        print("\n👋 Sistema detenido por el usuario")
    except Exception as e:
        print(f"❌ Error crítico: {str(e)}")
        traceback.print_exc()


if __name__ == "__main__":
    main()