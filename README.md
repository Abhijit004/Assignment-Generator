# Assignment-Generator
 <img width="913" alt="Screenshot 2023-08-05 090424" src="https://github.com/Abhijit004/Assignment-Generator/assets/133393475/ed250804-baf5-4c93-ac27-eb1dcd4317ba">

A small Python program to take filename inputs and generate a Assignment report out of them with html and css.
## Aim behind this Program :gem:
When it comes to creating a proper report of any assignment(containing codes and all), I wished if there could exist a program which would take my filepaths as input and generate the report for me, where every code block would be prettified(in word editor, a picture insertion ~ destruction :sweat:). Since I failed to find one, I created one for myself :sweat_smile:

## Some Implementation details :hammer_and_pick:
* The program is heavily inspired by [Stackedit's](https://stackedit.io) Markdown to HTML rendering. I highly recommend using **Stackedit** for any markdown related works (I am writing this `README.md` using Stackedit only :grin:)

* I used Python [Pygments](https://pygments.org/) module to accomplish the task of prettifying the code. After finding out that the builtin CLexer is not rendering as per my wish, I had to create one for myself, where, without [ChatGPT](https://chat.openai.com/) it would have taken a huge amount of my time.
*  The program generates a **report.html file**. One needs to open it via any web browser and use the `print to pdf` functionality or use [sejda](https://www.sejda.com/html-to-pdf) to convert that HTML to a pdf (I recommend the latter as it won't break your HTML into pages).

## Usage :computer:
Download the `toHTML.py` file from github, open terminal in the same directory where it is downloaded, and run the following command (please, first install `Python`)
```bash
pip install Pygments
python toHTML.py
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
