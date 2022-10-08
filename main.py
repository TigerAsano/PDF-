q_f = f"どの処理をしたいですが？(数字)\n 1. PDFの結合\n 2. PDFの分割\n\n---> "
index = int(input(q_f))
if index==1:
  filename = input("\n\n処理後のファイル名を入力してください。\n\n--->\n\n")
  print(PDF_Converter.combine(filename))
elif index==2:
  print(PDF_Converter.split())
else:
  print("正しい番号を入力してください。")
