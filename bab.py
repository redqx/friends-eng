def process_scene_lines(input_file, output_file):
    scene_number = 1  # 用于计数的场景编号

    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            if line.startswith('[Scene'):
                line = line.replace(']', '')
                # 格式化场景行
                formatted_line = f'## [Scene {scene_number:02d}]'
                # 写入格式化场景
                outfile.write(formatted_line + '\n\n')
                # 写入后面的内容
                
                content_line = line[len('[Scene'):]  # 获取内容部分
                outfile.write(content_line)  # 写入下一行
                scene_number += 1  # 更新场景编号
            else:
                # 如果不是场景行，原样写入
                outfile.write(line)
            
            outfile.write('\n')

# 使用示例
process_scene_lines(r'D:\mm_github\redqx\friends-eng\season-01\03 The One With the Thumb\index.md', 'output.txt')