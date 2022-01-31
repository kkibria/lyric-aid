import argparse
import os
import webview
import prosodic as p

p.being.config['print_to_screen']=0
p.config['print_to_screen']=0
DEFAULT_METER='default_english'

# API to the webview
class Api():
    def checkText(self, text):
        # print(text)
        m = p.config['meters'][DEFAULT_METER]
        t = p.Text(filename=text, lang='en', meter=m)
        t.parse(m)
        lines = []
        for parse in t.bestParses():
            output = []
            for pos in parse.positions:
                x=str(pos)
                if pos.has_viol: x+='*'
                output.append(x)
            lines.append(output)
        # print(lines)
        return lines

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
    # s = "of mans first disobedience and the fruit\nbrought death into the world and all"
    # r = api.checkText(s)
    # print(r)

