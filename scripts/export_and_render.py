import os
import sys
import win32com.client

sys.stdout.reconfigure(encoding='utf-8')

os.makedirs("rendered_slides", exist_ok=True)

pptx_abs = os.path.abspath("SPATIAL_SENSE_Theme2_Vishwakarma_2026_27.pptx")
pdf_abs = os.path.abspath("SPATIAL_SENSE_Theme2_Presentation.pdf")

print(f"Opening {pptx_abs} in PowerPoint...")
powerpoint = win32com.client.Dispatch("PowerPoint.Application")
# Keep it invisible or minimized if possible
presentation = powerpoint.Presentations.Open(pptx_abs, WithWindow=False)

print(f"Exporting to PDF: {pdf_abs}...")
# 32 is the constant for ppSaveAsPDF
presentation.SaveAs(pdf_abs, 32)
print("PDF exported successfully.")

print("Exporting slides to PNG images...")
for idx, slide in enumerate(presentation.Slides, 1):
    png_path = os.path.abspath(f"rendered_slides/slide_{idx}.png")
    # Export slide as PNG with 1920x1080 resolution
    slide.Export(png_path, "PNG", 1920, 1080)
    print(f"  Slide {idx} exported to rendered_slides/slide_{idx}.png")

presentation.Close()
powerpoint.Quit()
print("Export and rendering complete.")
