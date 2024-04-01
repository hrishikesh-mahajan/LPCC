/*** Definition section ***/
%{
    #include "y.tab.h"
%}

/*** Rules section ***/
%%

He |
She |
We |
They { return NOUN; }

is |
will |
shall |
running |
ran |
run { return VERB; }

well |
quickly |
fast { return ADVERB; }

%%
