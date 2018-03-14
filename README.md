# ReverseX
Tool for extracting source code of browsers(Chrome, Firefox, Safari, Brave) extension/add-on.
## Installation
```
git clone https://github.com/chrsow/ReverseX.git
cd ReverseX
// pip for python3
pip3 install -r requirements
```

_I'm finding a way to make the program be installed with pip._
## Usage
```
python ./ReverseX/ReverseX.py <command> <arguments>
```

Commands (using Safari as an example).

| Function  | Command               | Notes
| :------ | :-------------------- | :---------
| list    | `ReverseX safari ls`  | Lists all Safari extension on user's computer.
| extract | `ReverseX safari extract ABC` | Extracts Safari extension ABC on default folder (`./ReverseX/Data/Safari`).
| extract | `ReverseX safari extract ABC /tmp` | Extracts Safari extension ABC on specific folder (e.g. `/tmp`).
## TODO

### Support for multi OS
- [ ] Windows
    - [ ] Chrome
    - [ ] Firefox
    - [ ] Safari
    - [ ] Brave
- [ ] Linux
    - [ ] Chrome
    - [ ] Firefox
    - [ ] Safari
    - [ ] Brave
- [ ] MacOS
    - [ ] Chrome
    - [ ] Firefox
    - [x] Safari
    - [ ] Brave
### Aesthetic
- [ ] Add more color on command output.

### Search & Extract
- [ ] Searchs extension online, downloads and extracts. 

## Contribution
All contributions are welcome, PR or send any issue and we are good to go.