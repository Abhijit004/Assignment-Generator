# Assignment-Generator
<img width="948" alt="banner" src="https://github.com/Abhijit004/Assignment-Generator/assets/133393475/2b391046-ebc5-4142-b968-f013dd528e61">


A small C program to take filename inputs and generate a Assignment report out of them with html and css.
## Aim behind this Program :gem:
When it comes to creating a proper report of any assignment(containing codes and all), I wished if there could exist a program which would take my filepaths as input and generate the report for me, where every code block would be prettified(in word editor, a picture insertion ~ destruction :sweat:). Since I failed to find one, I created one for myself :sweat_smile:

## Some Implementation details :hammer_and_pick:
* The `c` file does the heavy lifting of taking input from the user and generating stylised html as per it. 
* Styles of the html file are heavily inspired by [StackEdit](https://stackedit.io/), a great online markdown editor. Infact, this README is created in Stackedit's editor only :grin:!
* I am using [Prism](https://prismjs.com/),  a lightweight, extensible syntax highlighter for highlighting the code blocks, it works stunningly great !
## Usage :computer:
* Download three files from here:
  * prism.js
  * prism.css
  * toHTML.c
* Run the c file `toHTML.c`. Thats it !
```bash
gcc toHTML.c -o toHTML && ./toHTML
```

## Detailed working process :gear:
* **Take user details**
  * Name
  * Group(HX/HY)
  * Enrollment no
* **Take Assignment details**
  * Assignment number
  * No of Questions
* **Via a loop, for every Question**
  * Take Question statement
  * Take the `.c` file containing the code
  * Take as many `png` images the user wishes to have for that question
* **Ask for a confirmation**
* **The final product: `report.html`**

<img width="707" alt="Screenshot" src="https://github.com/Abhijit004/Assignment-Generator/assets/133393475/008ddce4-5f78-404f-be16-64ecf972e8dd">

## Licence
The project is under [MIT License](./LICENSE)
