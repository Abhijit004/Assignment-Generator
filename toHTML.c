#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void replaceSubstring(char *str, const char *oldSubstr, const char *newSubstr) {
    int oldLen = strlen(oldSubstr);
    int newLen = strlen(newSubstr);
    char *ptr = strstr(str, oldSubstr);
    while (ptr != NULL) {
        // Calculate the length of the remaining string
        int remainingLen = strlen(ptr + oldLen);

        // Shift the remaining characters to accommodate the new substring
        memmove(ptr + newLen, ptr + oldLen, remainingLen + 1);

        // Copy the new substring
        memcpy(ptr, newSubstr, newLen);

        // Search for the next occurrence
        ptr = strstr(ptr + newLen, oldSubstr);
    }
}

int main() {
    char name[100];
    char group[100];
    char roll[100];
    char assignmentNo[100];
    int qno;

    // User input
    printf("Name: ");
    fgets(name, sizeof(name), stdin);
    name[strcspn(name, "\n")] = '\0';

    printf("Group: ");
    fgets(group, sizeof(group), stdin);
    group[strcspn(group, "\n")] = '\0';

    printf("Roll No: ");
    fgets(roll, sizeof(roll), stdin);
    roll[strcspn(roll, "\n")] = '\0';

    printf("Assignment No: ");
    fgets(assignmentNo, sizeof(assignmentNo), stdin);
    assignmentNo[strcspn(assignmentNo, "\n")] = '\0';

    printf("No of Questions: ");
    scanf("%d", &qno);
    getchar(); // Consume the newline character

    // Construct HTML code
    char *htmlcode;
    int bufferSize = 10000; // Adjust buffer size as needed
    htmlcode = (char *)malloc(bufferSize);
    snprintf(htmlcode, bufferSize,
             "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><title>Code block rendering</title><link rel=\"stylesheet\" href=\"prism.css\"/><script src=\"prism.js\" defer></script></head><body class='stackedit'><div class='stackedit__html'>Name: %s<br>Group: %s<br>RollNo: %s<br><h1>&#128203;Assignment %s</h1>",
             name, group, roll, assignmentNo);

    // Menu driven input
    for (int i = 1; i <= qno; i++) {
        char qLine[1000];
        char cfile[100];
        char output[1000];

        printf("\tQline: ");
        fgets(qLine, sizeof(qLine), stdin);
        qLine[strcspn(qLine, "\n")] = '\0';

        printf("\tC file: ");
        fgets(cfile, sizeof(cfile), stdin);
        cfile[strcspn(cfile, "\n")] = '\0';

        printf("\tPng files sep by space: ");
        fgets(output, sizeof(output), stdin);
        output[strcspn(output, "\n")] = '\0';

        FILE *f = fopen(cfile, "r");
        if (f == NULL) {
            perror("Error opening file");
            return 1;
        }
        char text[10000]; // Adjust buffer size as needed
        fread(text, 1, sizeof(text), f);

        replaceSubstring(text, "<", "&lt;");
        replaceSubstring(text, ">", "&gt;");

        fclose(f);

        char temp[10000]; // Adjust buffer size as needed
        snprintf(temp, sizeof(temp), "<h3>%s</h3><p><strong>Code</strong></p><pre class='line-numbers'><code class='language-c'>%s</code></pre><p><strong>Output</strong></p>", qLine, text);
        strcat(htmlcode, temp);

        char *token = strtok(output, " ");
        while (token != NULL) {
            snprintf(temp, sizeof(temp), "<img src=\"%s\">", token);
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
        perror("Error opening file");
        return 1;
    }
    fputs(htmlcode, outputFile);
    fclose(outputFile);

    free(htmlcode);
    printf("Process completed, please find a file named report.html on this directory\n");

    return 0;
}
