label foursome2:

$ dahliarounds = 0
$ jasmine_rounds = 0
$ iris_rounds = 0
label round_one:
menu:
    "Choose Dahlia":
        jump dahliaround01
    "Choose Jasmine.":
        jump jasmine_round01
    "Choose Iris.":
        jump iris_round01
############
label round_two:
    menu:
        "Choose Dahlia":
            if dahliarounds == 0:
                jump dahliaround01
            elif dahliarounds == 1:
                jump dahliaround02
        "Choose Jasmine":
            if jasmine_rounds == 0:
                jump jasmine_round01
            elif jasmine_rounds == 1:
                jump jasmine_round02
        "Choose Iris.":
            if iris_rounds == 0:
                jump iris_round01
            elif iris_rounds == 1:
                jump iris_round02
        
#############
label round_three:
    menu:
        "Choose Dahlia":
            if dahliarounds == 0:
                jump dahliaround01
            elif dahliarounds == 1:
                jump dahliaround02
            elif dahliarounds == 2:
                jump dahliaround03

        "Choose Jasmine":
            if jasmine_rounds == 0:
                jump jasmine_round01
            elif jasmine_rounds == 1:
                jump jasmine_round02
            elif jasmine_rounds == 2:
                jump jasmine_round03
            
        "Choose Iris.":
            if iris_rounds == 0:
                jump iris_round01
            elif iris_rounds == 1:
                jump iris_round02
            elif iris_rounds == 2:
                jump iris_round03
        
        
        
        
        
        
        
        
        
        







###DAHLIA####
label dahliaround01:
    $ dahliarounds +=1
    sch900 "I knew, you wouldn't be able to resist."
    jump round_two
label dahliaround02:
    $ dahliarounds +=1
    sch900 "Starting to feel it!"
    jump round_three
label dahliaround03:
    $ dahliarounds +=1
    sch900 "Cumming!"
    
    
####JASMINE#######
label jasmine_round01:
    $ jasmine_rounds +=1
    j "I knew, you wouldn't be able to resist."
    jump round_two
label jasmine_round02:
    $ jasmine_rounds +=1
    j "Starting to feel it! +1 "
    jump round_three
label jasmine_round03:
    $ jasmine_rounds +=1
    j "Cumming!"
    
####IRIS#######
label iris_round01:
    $ iris_rounds +=1
    sch1100 "I knew, you wouldn't be able to resist."
    jump round_two
label iris_round02:
    $ iris_rounds +=1
    sch1100 "Starting to feel it!"
    jump round_three
label iris_round03:
    $ iris_rounds +=1
    sch1100 "Cumming!"