# mammals-bayesdb
Ipython notebook for doing crosscat analysis of EOL mammals 'trait' data

You'll need a dump of mammals traits.  There is a script to make such dumps in the `eol_website` repository at
`[lib/traits_dumper.rb](https://github.com/EOL/eol_website/blob/master/lib/traits_dumper.rb)`

so you would say something like

    ID=1642 CHUNK=20000 TOKEN=`cat ../api.token` time ruby -r ./lib/traits_dumper.rb -e TraitsDumper.main

where api.token comes from `[services/authenticate](https://eol.org/services/authenticate)`.  (Currently your EOL account
needs to have 'power user' privilege.)

(1642 is the EOL page id for mammals)

I ran this on the 'google cloud'.  You could try it on an ordinary
compute server, but crosscat can be pretty compute intensive so you'll
probably want lots of cores and RAM.

GPL
