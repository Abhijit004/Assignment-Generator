#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void replaceSubstring(char *str, const char *oldSubstr, const char *newSubstr) {
    char *ptr = strstr(str, oldSubstr);
    while (ptr != NULL) {
        memmove(ptr + strlen(newSubstr), ptr + strlen(oldSubstr), strlen(ptr + strlen(oldSubstr)) + 1);
        memcpy(ptr, newSubstr, strlen(newSubstr));
        ptr = strstr(ptr + strlen(newSubstr), oldSubstr);
    }
}

void clearInputBuffer() {
    int c;
    do {
        c = getchar();
    } while (c != '\n');
}

void readFile(FILE *f, char text[]) {
    char ch; int i=0;
    while ((ch = fgetc(f)) != EOF) {
        text[i++] = ch;
    }
    text[i++] = '\0';
    fclose(f);
}

int main () {
    char name[100], group[100], roll[100], assignmentNo[100];
    int qno;

    //User input
    printf("Name: "); gets(name);
    printf("Group: "); gets(group);
    printf("roll: "); gets(roll);
    printf("Assignment No: "); gets(assignmentNo);
    printf("No of Questions: "); scanf("%d", &qno);

    char* htmlcode = (char *) malloc(1000000);

    snprintf(htmlcode, 10000000,
             "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><title>Report</title><link rel=\"stylesheet\" href=\"prism.css\"/><script src=\"prism.js\" defer></script></head><body class='stackedit'><div class='stackedit__html'><hr><p contenteditable=\"true\">Name: %s<br>Group: %s<br>RollNo: %s<br></p><h1 contenteditable=\"true\">&#128203;Assignment %s</h1>",
             name, group, roll, assignmentNo);

    // Menu driven input 
    clearInputBuffer();
    for (int i = 1; i <= qno; i++) {
        char qLine[1000];
        char cfile[100];
        char output[1000];
        
        printf("\tQline: "); gets(qLine);
        printf("\tC file: ");gets(cfile);
        printf("\tPng files sep by space: "); gets(output);

        FILE *f = fopen(cfile, "r");
        if (f == NULL) {
            printf("The given C file does not exist. Try giving again\n\n");
            i -= 1; continue;
        }

        char text[10000];
        readFile(f, text);
        // replacing the < and > tags
        replaceSubstring(text, "<", "&lt;");
        replaceSubstring(text, ">", "&gt;");

        char temp[10000]; // Adjust buffer size as needed
        snprintf(temp, sizeof(temp), "<h3 contenteditable=\"true\">%s</h3><pre class='line-numbers'><code class='language-c'>%s</code></pre>", qLine, text);
        strcat(htmlcode, temp);

        char *token = strtok(output, " ");
        while (token != NULL) {
            snprintf(temp, sizeof(temp), "<div class=\"imgdiv\"><img src=\"%s\"></div>", token);
            strcat(htmlcode, temp);

            token = strtok(NULL, " ");
        }
        strcat(htmlcode, "<hr>");
        printf("\n");
    }

    strcat(htmlcode, "</div></body></html>");

    // Writing to file
    FILE *outputFile = fopen("report.html", "w");
    if (outputFile == NULL) {
        printf("Error opening HTML file\n");
        return 1;
    }
    //write htmlCode
    fputs(htmlcode, outputFile);
    fclose(outputFile);

    free(htmlcode);
    printf("Process completed, please find a file named report.html on this directory\n");

    return 0;
}
