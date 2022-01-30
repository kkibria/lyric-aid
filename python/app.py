import argparse
import os
import webview
import prosodic as p

# API to the webview
class Api():
    def checkText(self, text):
        t = p.Text(text)
        # t.parse()
        # for parse in t.bestParses():
        #     print (parse)

    def toggleFullscreen(self):
        webview.windows[0].toggle_fullscreen()

    def sayHello(self):
        print("Hello")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='lyric-aid')
    parser.add_argument("-d", "--dev", action="store_true",
                           help="dev mode")
    args = parser.parse_args()
    api = Api()
    webview.create_window('Lyric Aid', url='../public/index.html', js_api=api, min_size=(600, 450))
    webview.start(debug=args.dev)
