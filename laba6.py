text = input()
replace_count = text.count('а')
replaced_text = text.replace('а', 'о')
symbol_count = len(text)
print(f"Исходная строка: {text}")
print(f"Строка с заменой: {replaced_text}")
print(f"Количество замен: {replace_count}")
print(f"Количество символов в строке: {symbol_count}")