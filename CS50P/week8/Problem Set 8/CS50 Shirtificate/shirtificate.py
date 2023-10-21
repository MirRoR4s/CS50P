from fpdf import FPDF, Align


class PDF(FPDF):
    def header(self):
        # 定义页眉字体样式
        self.set_font(family="Times", style="B", size=40)
        # 居中绘制页眉文本
        self.cell(text="CS50 Shirtificate", center=True, new_x="LMARGIN", new_y="NEXT", align='C')
        # 换行？
        self.ln(15)

    def drew_image(self):
        # 绘制图片
        self.image("D:\CS50P\CS50P\Week8\Problem Set 8\CS50 Shirtificate\shirtificate.png", x=Align.C, w=self.epw, h=self.eph)

    def drew_txt(self, name):
        # 光标上移
        self.set_y(100)
        # 将文字覆盖在图上，注意是白色的字体
        self.set_font("Times",size=30)
        self.set_text_color(r=255, g=255, b=255)
        self.cell(text=f"{name} took CS50", center=True)

def main():
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=False)
    pdf.header()
    pdf.drew_image()
    pdf.drew_txt(input("name: "))
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()