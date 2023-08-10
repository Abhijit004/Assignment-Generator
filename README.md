# Assignment-Generator
<img width="948" alt="banner" src="https://github.com/Abhijit004/Assignment-Generator/assets/133393475/2b391046-ebc5-4142-b968-f013dd528e61">


A small C program to take filename inputs and generate a Assignment report out of them with html and css.
## Aim behind this Program :gem:
When it comes to creating a proper report of any assignment(containing codes and all), I wished if there could exist a program which would _take my filepaths as input and generate the report_ for me, where every code block would be prettified(in word editor, a picture insertion ~ destruction :sweat:). Since I failed to find one, I created one for myself :sweat_smile:

## Some Implementation details :hammer_and_pick:
* The `c` file does the heavy lifting of taking input from the user and generating stylised html as per it. 
* Styles of the html file are heavily inspired by [StackEdit](https://stackedit.io/), a great online markdown editor. Infact, this README is created in Stackedit's editor only :grin:!
* I am using [Prism](https://prismjs.com/),  a lightweight, extensible syntax highlighter for highlighting the code blocks, it works stunningly great !
## Usage :computer:
* Download these three files from here:
  * `prism.js`
  * `prism.css`
  * `toHTML.c`
* Run the c file `toHTML.c`. Thats it !

Linux
```bash
gcc toHTML.c -o toHTML && ./toHTML
```
Windows
```bash
gcc toHTML.c -o toHTML && toHTML
```

## Detailed working process :gear:
* **Take user details**
  * Name
  * Group
  * roll no
* **Take Assignment details**
  * Assignment number
  * No of Questions
* **Via a loop, for every Question**
  * Take Question statement
  * Take the `.c` file path containing the code
  * Take as many `png` image paths the user wishes to have for that question (separated by space)
* **The final product: `report.html`** will be generated.

  <img width="638" alt="image" src="https://github.com/Abhijit004/Assignment-Generator/assets/133393475/36bb9b94-9d75-4b6a-a009-52fc9e976db6">

* Convert this html into a pdf by using `print to pdf` functionality of any web browser.
* **[Optional]** If you want, that the pdf does not break into pages, I have a trick for you. Add this text into prism.css file:
  ```css
  @media print {
    /* Adjust page size for printing */
    @page {
      size: 310mm 500mm; /*increase the '500mm'*/
    }
  }
  ```
  Increase the `500mm` to as large as you want to have your whole content set in 1 page.
## Things to keep in mind :bangbang:
* Keep the three files, `toHTML.c`, `prism.js`, `prism.css` in the same directory. Else, no Styling would occur.
* Dont use any online html to pdf converter tool. Your images will not be there.

## Licence
The project is under [MIT License](./LICENSE)
