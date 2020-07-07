filename = r"\\192.168.1.99\sda1\onecloud\crawl\crawltest.txt"

def writenas():
    with open(filename, 'a') as fp:
        fp.write("hello nas!")


if __name__ == "__main__":
    writenas()