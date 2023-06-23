# 指定文件路径
path = './Info.fcpxml'

# 时间从X/Y转化为X秒
def fraction_to_float(fraction_string):
    numerator, denominator = fraction_string.split('/')
    return float(numerator) / float(denominator)

# 时间从X秒转化为X分：Y秒
def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return '{:02d}:{:02d}'.format(int(minutes), int(seconds))


# 逐行读取文件，检索，打印
with open(path, "r") as f:
    for line in f:
        if "<chapter-marker start=\"" in line and "s\"" in line:
            timestart = line.index("start=\"") + len("start=\"")
            timeend = line.index("s\"")
            timemarker = line[timestart:timeend]
            timemarker = format_time(fraction_to_float(timemarker))
            commentstart = line.index("value=\"") + len("value=\"")
            commentend = line.index("\" posterOffset")
            comment = line[commentstart:commentend]
            TimeMarkerComment =str(timemarker + ' ' + comment)
            print(TimeMarkerComment)
