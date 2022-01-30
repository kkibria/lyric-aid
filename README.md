> Note: `pip install pywebview` with python 3.9 will give error.
> See article [How to fix error during pythonnet installation](https://stackoverflow.com/questions/67418533/how-to-fix-error-during-pythonnet-installation).
> Download [pythonnet-2.5.2-cp39-cp39-win_amd64.whl](https://download.lfd.uci.edu/pythonlibs/x6hvwk7i/pythonnet-2.5.2-cp39-cp39-win_amd64.whl) first.

Powershell
```
Invoke-WebRequest -Uri https://download.lfd.uci.edu/pythonlibs/x6hvwk7i/pythonnet-2.5.2-cp39-cp39-win_amd64.whl -OutFile pythonnet-2.5.2-cp39-cp39-win_amd64.whl
```

```bash
pip install pythonnet-2.5.2-cp39-cp39-win_amd64.whl
pip install pywebview
pip install git+git://github.com/quadrismegistus/prosodic.git
npx degit --force sveltejs/template
node scripts/setupTypeScript.js
npm install
```
