%{
%}

%%

"run"|"walk"|"eat"|"sleep" {
    printf("Verb : %s\n", yytext);
}

"I"|"you"|"he"|"she"|"it"|"we"|"they" {
    printf("Pronoun : %s\n", yytext);
}

"quickly"|"slowly"|"happily"|"sadly" {
    printf("Adverb : %s\n", yytext);
}

"dog"|"cat"|"car"|"tree" {
    printf("Noun : %s\n", yytext);
}

[\n\t ]+ { /* Ignore whitespace, newline, tab */ }

. {
    printf("Unknown : %s\n", yytext);
}

%%

int yywrap() {
    return 1;
}

int main(int argc, char *argv[]) {
    ++argv, --argc;  /* skip over program name */
    if (argc > 0)
        yyin = fopen(argv[0], "r");
    else
        yyin = stdin;

    yylex();
}

