import argparse


def convert_indent(text, to_tabs=False):
	"""
	根据输入参数，将文本中的缩进从4个空格转换为tab，或者从tab转换为4个空格。
	
	参数:
		text (str): 需要转换的文本。
		to_tabs (bool): 如果为True，将4个空格转换为tab；如果为False，将tab转换为4个空格。
	
	返回:
		str: 转换后的文本。
	"""
	if to_tabs:
		return text.replace('    ', '\t')  # 4个空格替换为tab
	else:
		return text.replace('\t', '    ')  # tab替换为4个空格


def process_file(input_file, output_file=None, to_tabs=False):
	"""
	处理文件，转换缩进并将结果写回文件或输出到其他文件。
	
	参数:
		input_file (str): 输入文件路径。
		output_file (str): 输出文件路径。如果为None，则就地修改。
		to_tabs (bool): 如果为True，将4个空格转换为tab；如果为False，将tab转换为4个空格。
	"""
	with open(input_file, 'r', encoding='utf-8') as infile:
		content = infile.read()
	
	# 转换缩进
	converted_content = convert_indent(content, to_tabs)

	# 如果没有输出文件，则覆盖输入文件
	if output_file is None:
		output_file = input_file

	with open(output_file, 'w', encoding='utf-8') as outfile:
		outfile.write(converted_content)


def main():
	# 创建命令行参数解析器
	parser = argparse.ArgumentParser(description="Convert indentation between tabs and 4 spaces.")
	
	# 添加命令行参数
	parser.add_argument('input_file', type=str, help="Input file path")
	parser.add_argument('output_file', type=str, nargs='?', help="Output file path (optional)")
	parser.add_argument('--to_tabs', action='store_true', help="Convert 4 spaces to tabs")
	
	# 解析参数
	args = parser.parse_args()

	# 判断是否指定了 output_file，如果没有则就地修改
	output_file = args.output_file if args.output_file else None

	# 如果没有指定 --to_tabs，则默认将tab转换为4个空格
	to_tabs = args.to_tabs

	# 调用处理文件的函数
	process_file(args.input_file, output_file, to_tabs)


if __name__ == "__main__":
	main()
