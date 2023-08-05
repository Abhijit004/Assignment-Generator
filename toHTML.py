from pygments import highlight
from pygments.formatters import HtmlFormatter




# The code for CustomCLexer starts here
from pygments.lexer import RegexLexer
from pygments.token import Text, Comment, Keyword, Name, String, Number, Operator

class CustomCLexer(RegexLexer):
    name = 'CustomC'
    aliases = ['customc']
    filenames = ['*.c']

    tokens = {
        'root': [
            # Whitespace and comments
            #(r'\s+|[{}|:;,.]', Text),
            (r'\/\/.*?$', Comment.Single),
            (r'\/\*[\s\S]*?\*\/', Comment.Multiline),
            (r'<\w*.h>', Number),

            (r'#(include|define|ifdef|ifndef|endif|if|elif|else|pragma|error|warning|line|undef|include_next)\b', Comment.Special),

            # Keywords (blue)
            (r'\b(auto|break|case|char|const|continue|default|do|double|'
             r'else|enum|extern|float|for|goto|if|register|'
             r'return|short|signed|sizeof|static|struct|switch|typedef|'
             r'union|unsigned|void|volatile|while)\b', Keyword),

            (r'int|float|long|char|short|double|void|bool', Keyword.Constant),

            # Function definitions (green)
            (r'\b([A-Za-z_]\w*)\s*(?=\()', Name.Function), 

            # Symbols (red)
            (r'[&\[\]\*\|\=\-\+\>\<\/]', Operator),

            # Function arguments (orange)
            (r'\b[A-Za-z_]\w*\b(?=\s*\()', Name.Variable),

            # Data types (blue)
            (r'\b(char|short|int|long|float|double|void)\b', Keyword.Type),

            # Strings
            (r'"(\\.|[^"])*"', String),

            # Numbers (purple)
            (r'\b[A-Z]+\b|\b\d+\b', Number),

            # Escape sequences (purple)
            (r'\\[^\s]', Number),

            # Identifiers
            (r'\b[A-Za-z_]\w*\b|[,.;:<>{}()]', Name),

            # Anything else
            (r'.', Text),
        ]
    }

# The code for CustomCLexer end here




#Menu driven program
NAME = input("Your name: ")
ROLL = input("Your roll: ")
GROUP = input("Your group(HX/HY): ")

ano = int(input("Assignment no: "))
noOfQs = int(input("No of Q: "))
c_files, Qs, images = [], [], []

for i in range(noOfQs):
    Qs.append(input(f"\tEnter Q {i+1}: "))
    c_files.append(input(f"\tEnter C file {i+1}: "))
    images.append(input("\tEnter png of that(space separated if more than one): ").split())
    print()

final = (input("Are you satisfied with the inputs? (0/1): "))
if final == '0':
    print("okay, try again")
    exit()
else:
    print("Started processing ..... please wait")

#preparing the html code
htmlCode = '''
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Report</title>
</head>
<style>
@import url('https://fonts.googleapis.com/css2?family=Fira+Mono:wght@400&family=Poppins:wght@500&display=swap');

/* markdown css*/

html {
    line-height: 1.15;
    -ms-text-size-adjust: 100%;
    -webkit-text-size-adjust: 100%
}

body {
    margin: 0;
    background-color: hsl(0, 0%, 100%);
    color:#2e2e2e;
    font-family: 'Poppins', sans-serif;
}

h1 {
    font-size: 2em;
    margin: .67em 0
}

hr {
    box-sizing: content-box;
    height: 0;
    overflow: visible
}

b,
strong {
    font-weight: inherit;
    font-weight: bolder;
}



img {
    border-style: none;
    border-radius: 0.5em;
}


/*html {
    color: rgba(0, 0, 0, .75);
    font-size: 16px;
    font-family: Lato, Helvetica Neue, Helvetica, sans-serif;
    font-variant-ligatures: common-ligatures;
    line-height: 1.67;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale
}*/

blockquote,
dl,
ol,
p,
pre,
ul {
    margin: 1.2em 0
}

h1,
h2,
h3,
h4,
h5,
h6 {
    margin: 1.8em 0;
    line-height: 1.33
}

h1:after,
h2:after {
    content: '';
    display: block;
    position: relative;
    top: .33em;
    border-bottom: 4px solid hsla(0, 0%, 50%, .33)
}

ol ol,
ol ul,
ul ol,
ul ul {
    margin: 0
}

dt {
    font-weight: 700
}



hr {
    border: 0;
    border-top: 4px solid hsla(0, 0%, 50%, .33);
    margin: 2em 0
}

.toc ul {
    list-style-type: none;
    padding-left: 20px
}

table {
    background-color: transparent;
    border-collapse: collapse;
    border-spacing: 0
}

td,
th {
    border-right: 1px solid #dcdcdc;
    padding: 8px 12px
}

td:last-child,
th:last-child {
    border-right: 0
}

td {
    border-top: 1px solid #dcdcdc
}

img {
    width: 100%
}

.stackedit__html {
    margin-bottom: 180px;
    margin-left: auto;
    margin-right: auto;
    padding-left: 30px;
    padding-right: 30px;
    max-width: 900px
}

.stackedit__toc ul {
    padding: 0
}

.stackedit__toc ul a {
    margin: .5rem 0;
    padding: .5rem 1rem
}

.stackedit__toc ul ul {
    color: #888;
    font-size: .9em
}

.stackedit__toc ul ul a {
    margin: 0;
    padding: .1rem 1rem
}

.stackedit__toc li {
    display: block
}

.stackedit__toc a {
    display: block;
    color: inherit;
    text-decoration: none
}

.stackedit__toc a:active,
.stackedit__toc a:focus,
.stackedit__toc a:hover {
    background-color: rgba(0, 0, 0, .075);
    border-radius: 3px
}

.stackedit--pdf blockquote {
    border-left-color: #ececec
}

.stackedit--pdf .katex-mathml,
.stackedit--pdf annotation {
    display: none
}

.stackedit--pdf .stackedit__html {
    padding-left: 0;
    padding-right: 0;
    max-width: none
}
/* end*/

.highlight {
    padding-right: 2em;
}

pre {
    background-color: #242424;
    font-size: 1rem;
    font-family: 'Fira Mono', monospace;
    padding: 1em;
    border-radius: 0.5em;
    overflow-x: auto;
    width: 100%;
}

pre {
    line-height: 125%;
}

td.linenos .normal {
    color: inherit;
    background-color: transparent;
    padding-left: 5px;
    padding-right: 5px;
}

span.linenos {
    color: inherit;
    background-color: transparent;
    padding-left: 5px;
    padding-right: 5px;
}

td.linenos .special {
    color: #000000;
    background-color: #ffffc0;
    padding-left: 5px;
    padding-right: 5px;
}

span.linenos.special {
    color: #000000;
    background-color: #ffffc0;
    padding-left: 5px;
    padding-right: 5px;
}

.hll {
    background-color: #49483e
}

.c {
    color: #75715e
}

/* Comment */
.err {
    color: #960050;
    background-color: #1e0010
}

/* Error */
.esc {
    color: #f8f8f2
}

/* Escape */
.g {
    color: #f8f8f2
}

/* Generic */
.k {
    color: #f92672;
}

/* Keyword */
.l {
    color: #ae81ff
}

/* Literal */
.n {
    color: #f2f2f8;
}

/* Name */
.o {
    color: #f92672;
}

/* Operator */
.x {
    color: #f2f8f4
}

/* Other */
.p {
    color: #f8f8f2
}

/* Punctuation */
.ch {
    color: #75715e
}

/* Comment.Hashbang */
.cm {
    color: #75715e
}

/* Comment.Multiline */
.cp {
    color: #f92672
}

/* Comment.Preproc */
.cpf {
    color: #e6db74
}

/* Comment.PreprocFile */
.c1 {
    color: #75715e
}

/* Comment.Single */
.cs {
    color: #f92672
}

/* Comment.Special */
.gd {
    color: #f92672
}

/* Generic.Deleted */
.ge {
    color: #f8f8f2;
    font-style: italic
}

/* Generic.Emph */
.gr {
    color: #f8f8f2
}

/* Generic.Error */
.gh {
    color: #f8f8f2
}

/* Generic.Heading */
.gi {
    color: #a6e22e
}

/* Generic.Inserted */
.go {
    color: #66d9ef
}

/* Generic.Output */
.gp {
    color: #f92672;
    font-weight: bold
}

/* Generic.Prompt */
.gs {
    color: #f8f8f2;
    font-weight: bold
}

/* Generic.Strong */
.gu {
    color: #75715e
}

/* Generic.Subheading */
.gt {
    color: #f8f8f2
}

/* Generic.Traceback */
.kc {
    color: #66d9ef;
    font-style: italic;
}

/* Keyword.Constant */
.kd {
    color: #66d9ef
}

/* Keyword.Declaration */
.kn {
    color: #f92672
}

/* Keyword.Namespace */
.kp {
    color: #66d9ef
}

/* Keyword.Pseudo */
.kr {
    color: #66d9ef
}

/* Keyword.Reserved */
.kt {
    color: #66d9ef
}

/* Keyword.Type */
.ld {
    color: #e6db74
}

/* Literal.Date */
.m {
    color: #ae81ff
}

/* Literal.Number */
.s {
    color: #e6db74
}

/* Literal.String */
.na {
    color: #a6e22e
}

/* Name.Attribute */
.nb {
    color: #f8f8f2
}

/* Name.Builtin */
.nc {
    color: #a6e22e
}

/* Name.Class */
.no {
    color: #66d9ef
}

/* Name.Constant */
.nd {
    color: #a6e22e
}

/* Name.Decorator */
.ni {
    color: #f8f8f2
}

/* Name.Entity */
.ne {
    color: #a6e22e
}

/* Name.Exception */
.nf {
    color: #a6e22e
}

/* Name.Function */
.nl {
    color: #a6e22e
}

/* Name.Label */
.nn {
    color: #f8f8f2
}

/* Name.Namespace */
.nx {
    color: #a6e22e
}

/* Name.Other */
.py {
    color: #f8f8f2
}

/* Name.Property */
.nt {
    color: #f92672
}

/* Name.Tag */
.nv {
    color: #f8f8f2
}

/* Name.Variable */
.ow {
    color: #f92672
}

/* Operator.Word */
.pm {
    color: #f8f8f2
}

/* Punctuation.Marker */
.w {
    color: #f8f8f2
}

/* Text.Whitespace */
.mb {
    color: #ae81ff
}

/* Literal.Number.Bin */
.mf {
    color: #ae81ff
}

/* Literal.Number.Float */
.mh {
    color: #ae81ff
}

/* Literal.Number.Hex */
.mi {
    color: #ae81ff
}

/* Literal.Number.Integer */
.mo {
    color: #ae81ff
}

/* Literal.Number.Oct */
.sa {
    color: #e6db74
}

/* Literal.String.Affix */
.sb {
    color: #e6db74
}

/* Literal.String.Backtick */
.sc {
    color: #e6db74
}

/* Literal.String.Char */
.dl {
    color: #e6db74
}

/* Literal.String.Delimiter */
.sd {
    color: #e6db74
}

/* Literal.String.Doc */
.s2 {
    color: #e6db74
}

/* Literal.String.Double */
.se {
    color: #ae81ff
}

/* Literal.String.Escape */
.sh {
    color: #e6db74
}

/* Literal.String.Heredoc */
.si {
    color: #e6db74
}

/* Literal.String.Interpol */
.sx {
    color: #e6db74
}

/* Literal.String.Other */
.sr {
    color: #e6db74
}

/* Literal.String.Regex */
.s1 {
    color: #e6db74
}

/* Literal.String.Single */
.ss {
    color: #e6db74
}

/* Literal.String.Symbol */
.bp {
    color: #f8f8f2
}

/* Name.Builtin.Pseudo */
.fm {
    color: #a6e22e
}

/* Name.Function.Magic */
.vc {
    color: #a6e22e
}

/* Name.Variable.Class */
.vg {
    color: #f8f8f2
}

/* Name.Variable.Global */
.vi {
    color: #f8f8f2
}

/* Name.Variable.Instance */
.vm {
    color: #f8f8f2
}

/* Name.Variable.Magic */
.il {
    color: #ae81ff
}

/* Literal.Number.Integer.Long */
</style>

<body class="stackedit">
    <div class="stackedit__html">
        Name:  username<br>
        Group: usergroup<br>
        Roll:  userroll<br>
        <h1 id="assignment-1">Assignment ano</h1>
'''.replace('ano', str(ano)).replace('username', NAME).replace('userroll', ROLL).replace('usergroup', GROUP)

for question, codefile, img in zip(Qs, c_files, images):
    with open(codefile, 'r') as f:
        code = f.read()
    code = code.replace('\t', ' '*4)
    
    htmlCode += f'''
    <h3>{question}</h3>
    <p><strong>Code</strong></p>
    {highlight(code, CustomCLexer(), HtmlFormatter())}
    <p><strong>Output</strong></p>
    '''
    for i in img:
        htmlCode += f'''
        <img src={i}>
        '''
    htmlCode += '''
    <hr>
    '''
    print("\tparcing c file done...")


htmlCode += '''
    </div>
</body>

</html>
'''

#writing the html code
with open("report.html", "w") as f:
    f.write(htmlCode)

#success-message
print("Task has been successful. Please find a file named report.html in this directory.")
