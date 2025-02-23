import streamlit as st
import random
import textwrap
from fpdf import FPDF

# Technical Blog Templates
TECHNICAL_BLOG_TEMPLATES = [
    "The importance of {keyword} in the tech industry cannot be overstated. In this article, we explore how {keyword} is revolutionizing various sectors.",
    "{keyword} is transforming the future of technology! Discover its core benefits and how it is shaping the digital landscape.",
    "Are you looking to master {keyword}? Here’s a complete guide to understanding and applying it effectively in real-world applications.",
]

# Non-Technical Blog Templates
NON_TECHNICAL_BLOG_TEMPLATES = [
    "The impact of {keyword} on our daily lives is undeniable. This article explores how {keyword} influences our world in surprising ways.",
    "Ever wondered how {keyword} can change the way we think and act? Let’s dive into its significance and practical applications.",
    "{keyword} plays a crucial role in shaping our lifestyle. Discover the key insights that make it so relevant today.",
]

def generate_blog(title, keyword, topic_type, length="medium"):
    """Generate a blog post dynamically based on topic type (Technical or Non-Technical)."""
    
    if topic_type == "Technical":
        template = random.choice(TECHNICAL_BLOG_TEMPLATES)
        body = (
            f"\n\n### The Power of {keyword}\n"
            f"{keyword} has transformed the way we think about technology and business. "
            f"It plays a crucial role in modern advancements.\n\n"
            f"### How to Use {keyword} Effectively\n"
            f"1. Understand its fundamentals.\n"
            f"2. Apply best practices.\n"
            f"3. Stay updated with trends.\n\n"
            f"**Why should you care?** {keyword} is revolutionizing industries worldwide."
        )
    else:
        template = random.choice(NON_TECHNICAL_BLOG_TEMPLATES)
        body = (
            f"\n\n### The Influence of {keyword}\n"
            f"{keyword} has had a profound impact on society, changing how we live, work, and interact with others.\n\n"
            f"### Why {keyword} Matters\n"
            f"1. It affects personal growth and mindset.\n"
            f"2. It drives social and cultural evolution.\n"
            f"3. It influences decision-making and everyday life.\n\n"
            f"**Why should you care?** Understanding {keyword} helps us adapt and thrive in an ever-changing world."
        )

    conclusion = f"\n\nIn conclusion, {keyword} continues to shape our future in meaningful ways. Staying informed and engaged is the key to leveraging its benefits."

    # Adjust blog length
    if length == "short":
        body = textwrap.shorten(body, width=300, placeholder="...")
    elif length == "long":
        body += "\n\n" + " ".join(["Here’s another perspective on " + keyword] * 5)

    blog_content = f"# {title}\n\n{template.format(keyword=keyword)}\n{body}\n{conclusion}"
    
    return blog_content

def save_as_pdf(blog_content):
    """Generate a PDF from the blog content."""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in blog_content.split("\n"):
        pdf.multi_cell(0, 10, line)

    pdf_file = "blog.pdf"
    pdf.output(pdf_file)
    return pdf_file

# Streamlit UI
st.title("📝 AI Blog Generator")
st.write("Generate an AI-powered blog by selecting a topic type, entering a title, and keyword.")

title = st.text_input("Enter Blog Title", "The Future of AI")
keyword = st.text_input("Enter Keyword", "Artificial Intelligence")

topic_type = st.radio("Select Topic Type", ["Technical", "Non-Technical"], index=0)
length = st.radio("Select Blog Length", ["Short", "Medium", "Long"], index=1)

if st.button("Generate Blog"):
    blog_content = generate_blog(title, keyword, topic_type, length.lower())
    st.session_state["blog_content"] = blog_content  # Store generated content
    st.subheader("📄 Generated Blog")
    st.write(blog_content)

if "blog_content" in st.session_state:
    if st.button("Download PDF"):
        pdf_path = save_as_pdf(st.session_state["blog_content"])
        with open(pdf_path, "rb") as f:
            st.download_button("📥 Download Blog as PDF", f, file_name="blog.pdf", mime="application/pdf")

st.write("🚀 **Now generate and download blogs instantly!**")

