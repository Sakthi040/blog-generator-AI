import streamlit as st
import random
import textwrap
from fpdf import FPDF

# Sample blog templates for AI-generated content
BLOG_TEMPLATES = [
    "The importance of {keyword} in today's world cannot be overstated. In this article, we explore how {keyword} is shaping industries and impacting lives.",
    "{keyword} is a game-changer! Discover the top benefits and how you can leverage {keyword} for success.",
    "Are you looking to master {keyword}? Here’s a complete guide to understanding and applying it effectively.",
]

def generate_blog(title, keyword, length="medium"):
    """Generate a structured blog post using a title and keyword."""
    
    template = random.choice(BLOG_TEMPLATES)
    intro = template.format(keyword=keyword)
    
    body = (
        f"\n\n### 🔹 The Power of {keyword}\n"
        f"{keyword} has transformed the way we think about technology and business. "
        f"It plays a crucial role in modern advancements.\n\n"
        f"### 🛠️ How to Use {keyword} Effectively\n"
        f"✅ Understand its fundamentals.\n"
        f"✅ Apply best practices.\n"
        f"✅ Stay updated with trends.\n\n"
        f"💡 **Why should you care?** {keyword} is not just a buzzword; it is revolutionizing industries worldwide."
    )
    
    conclusion = f"\n\n📌 **Conclusion:** {keyword} is a powerful tool that can drive innovation. Stay informed and make the most of it!"

    # Adjust blog length
    if length == "short":
        body = textwrap.shorten(body, width=300, placeholder="...")
    elif length == "long":
        body += "\n\n" + " ".join(["📝 Another perspective on " + keyword] * 5)

    blog_content = f"# {title}\n\n{intro}\n{body}\n{conclusion}"
    
    return blog_content

def save_as_pdf(title, blog_content):
    """Generate a well-formatted PDF from the blog content."""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Title Formatting
    pdf.set_font("Arial", style="B", size=16)
    pdf.multi_cell(0, 10, title, align="C")
    pdf.ln(10)

    # Body Formatting
    pdf.set_font("Arial", size=12)
    for line in blog_content.split("\n"):
        pdf.multi_cell(0, 10, line)

    pdf_file = "blog.pdf"
    pdf.output(pdf_file)
    return pdf_file

# Streamlit UI
st.set_page_config(page_title="AI Blog Generator", layout="centered")
st.title("📝 AI Blog Generator")
st.write("Generate an AI-powered blog with a **custom title & keyword.**")

# Sidebar for inputs
st.sidebar.header("🔧 Input Fields")
title = st.sidebar.text_input("📌 Enter Blog Title", "The Future of AI")
keyword = st.sidebar.text_input("🔑 Enter Keyword", "Artificial Intelligence")
length = st.sidebar.radio("📏 Select Blog Length", ["Short", "Medium", "Long"], index=1)

# Generate Blog
if st.sidebar.button("✨ Generate Blog"):
    blog_content = generate_blog(title, keyword, length.lower())
    st.session_state["blog_content"] = blog_content  # Store generated content
    st.subheader("📄 Generated Blog")
    st.write(blog_content)

    # Word Count
    word_count = len(blog_content.split())
    st.write(f"📊 **Word Count:** {word_count}")

# Download PDF
if "blog_content" in st.session_state:
    pdf_path = save_as_pdf(title, st.session_state["blog_content"])
    with open(pdf_path, "rb") as f:
        st.download_button("📥 Download Blog as PDF", f, file_name="blog.pdf", mime="application/pdf", help="Download your AI-generated blog as a PDF.")

st.sidebar.write("🚀 **Now generate & download AI-powered blogs instantly!**")
