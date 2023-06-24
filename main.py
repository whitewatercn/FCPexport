# 指定文件路径
path = './Info.fcpxml'

# 时间从X/Y转化为X秒
# 时间从X/Y转化为X秒
def fraction_to_float(fraction_string):
    if '/' in fraction_string:
        numerator, denominator = fraction_string.split('/')
        return float(numerator) / float(denominator)
    else:
        # 处理没有斜杠的情况，例如直接给定秒数的情况
        return float(fraction_string)


# 时间从X秒转化为X分：Y秒
def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return '{:02d}:{:02d}'.format(int(minutes), int(seconds))


# 逐行读取文件，检索，打印
FCPtimemarker = set()  # 用于储存时间标记和注释的集合
with open(path, "r") as fcpxml:
    for line in fcpxml:
        if "<chapter-marker start=\"" in line and "s\"" in line:
            # 提取时间标记
            timestart = line.index("start=\"") + len("start=\"")
            timeend = line.index("s\"")
            timemarker = line[timestart:timeend]
            timemarker_time = format_time(fraction_to_float(timemarker))
            # 提取注释
            commentstart = line.index("value=\"") + len("value=\"")
            commentend = line.index("\" posterOffset")
            comment = line[commentstart:commentend]
            TimeMarkerComment = str(timemarker_time + ' ' + comment)
            # 添加到集合中
            FCPtimemarker.add(TimeMarkerComment)
            # 打印时间标记和注释
            # print(TimeMarkerComment)

# 将时间标记和注释保存到文件
file_path = "./FCPtimemarker.txt"
with open(file_path, "w") as timemarkertxt:
    # 按照时间排序
    sorted_FCPtimemarker = sorted(FCPtimemarker, key=lambda x: x[:5])
    for line in sorted_FCPtimemarker:
        timemarkertxt.write(line + "\n")
