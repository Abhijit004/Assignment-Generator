# Assignment-Generator
<img width="948" alt="banner" src="https://github.com/Abhijit004/Assignment-Generator/assets/133393475/7ee36ac7-7925-4e39-8853-834c9b66b466">

A small C program to take filename inputs and generate a Assignment report out of them with html, css, js.
## :dart: Aim behind this Program 
When it comes to creating a proper report of any assignment(containing codes and all), I wished if there could exist a program which would _take my filepaths as input and generate the report_ for me, where every code block would be prettified(in word editor, a picture insertion ~ destruction :sweat:). Since I failed to find one, I created one for myself :sweat_smile:

## :hammer_and_pick: Some Implementation details 
* The c file does the heavy lifting of taking input from the user and generating stylised html as per it. 
* Styles of the html file are heavily inspired by **[StackEdit](https://stackedit.io/)**, a great online markdown editor. Infact, this README is created in Stackedit's editor only :grin:!
* I am using **[Prismjs](https://prismjs.com/)**,  a lightweight, extensible syntax highlighter for highlighting the code blocks, it works stunningly great :heart_eyes:!
* The css and js files are imported to the html from this github repository via **[JSDELIVR](https://www.jsdelivr.com/)**, *a free CDN for open source projects.*
## :computer: Usage 

* Download the c file `toHTML.c` from here and run it. Thats it :relieved:!

Linux
```bash
gcc toHTML.c -o toHTML && ./toHTML
```
Windows
```bash
gcc toHTML.c -o toHTML && toHTML
```

## :gear: Detailed working process 
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

* Convert this html into a pdf by using `print to pdf` functionality of the web browser you opened the html file with.
* The html elements(`question statement`, `user info`, `Assignment no`) are made **editable** , meaning you can *change them within html* if any typos arise while filling data in terminal.
* **[Optional]** If you want, that the pdf does not break into pages, I have a trick for you. Add this text into the generated report.html file inside headers:
```html
<style>
	@media print {
		/* Adjust page size for printing */
		@page {
			size: 310mm 500mm; /*increase the '500mm'*/
		}
	}
</style>
```
Increase the `500mm` to as large as you want to have your whole content set in 1 page.
## :scroll: Things to keep in mind 

* Don't use any online html to pdf converter tool. Your images will not be there.
* Give correct **paths** to the files (c files and png files) else you may face errors.
* The user **does not require to download the `prism.js` and `prism.css` files** for the tasks. It has been included in the repo for CDN to work.
* Currectly there is no feature to edit the code within HTML just like the question statements and all, assuming that the report will be made after finalising all the C codes ( However, it can be easily made possible with **[CodeMirror](https://codemirror.net/)**, *a code editor component for the web.* ).

## Licence
The project is under [MIT License](./LICENSE).
