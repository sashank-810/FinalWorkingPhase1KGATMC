from xhtml2pdf import pisa
import markdown
import io

def convert_markdown_to_pdf(markdown_text: str) -> bytes:
    """
    Converts markdown text to PDF bytes using xhtml2pdf.
    
    Args:
        markdown_text (str): Markdown content to be converted.

    Returns:
        bytes: PDF file content in bytes.
    """
    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_text)

    # Wrap in basic HTML structure with styling
    html = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
            }}
            h1, h2, h3 {{
                color: #2c3e50;
                border-bottom: 1px solid #ccc;
                padding-bottom: 5px;
            }}
            code {{
                background-color: #f4f4f4;
                padding: 2px 4px;
                border-radius: 4px;
                font-family: monospace;
            }}
            pre {{
                background-color: #f4f4f4;
                padding: 10px;
                border-radius: 4px;
                white-space: pre-wrap;
                word-wrap: break-word;
            }}
        </style>
    </head>
    <body>{html_content}</body>
    </html>
    """

    pdf_buffer = io.BytesIO()
    pisa_status = pisa.CreatePDF(src=html, dest=pdf_buffer)
    if pisa_status.err:
        raise RuntimeError("❌ PDF conversion failed.")
    
    return pdf_buffer.getvalue()
