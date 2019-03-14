# mammals-bayesdb
Ipython notebook for doing crosscat analysis of EOL mammals 'trait' data

I ran this on the 'google cloud' via docker (ask if you can't find the
docker image and maybe I can track it down).  You could try it on an
ordinary compute server, but crosscat can be pretty compute intensive
so you'll probably want lots of cores and RAM.

Bayesdb home: http://probcomp.csail.mit.edu/software/bayesdb/

Thanks to Ulli Schaechtle for help.

GPL

## Re-creating the mammals traits csv file

There's a snapshot in the repo but here is how you would make it:

There is a script to make traitdb dumps in the `eol_website` repository at
[`lib/traits_dumper.rb`](https://github.com/EOL/eol_website/blob/master/lib/traits_dumper.rb)

so you would say something like

    ID=1642 CHUNK=20000 TOKEN=`cat ../api.token` time ruby -r ./lib/traits_dumper.rb -e TraitsDumper.main

where api.token comes from [`services/authenticate`](https://eol.org/services/authenticate).  (Currently your EOL account
needs to have 'power user' privilege.)

[1642](https://eol.org/pages/1642) is the EOL page id for mammals.

