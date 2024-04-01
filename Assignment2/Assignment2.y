%{
    #include <stdio.h>
    void yyerror();
    int yylex();
%}

%token NOUN VERB ADVERB

%%
start: NOUN VERB ADVERB { printf("Valid Sentence.\n"); }
%%

int yywrap()
{
    return 0;
}

void yyerror()
{
    printf("Invalid Sentence.\n");
}

int main()
{
    printf("\n Enter English language sentence:\n");
    yyparse();
    yywrap();
}