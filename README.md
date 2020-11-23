# HackerSearch
This is me trying to build a search engine for programming related stuff.

Currently, however, it's just a bad frontend for SO

## Design Goals
This search engine should be privacy-respecting, return good results, and be fast in that order.

## Architecture
There's a bunch of folders in directory.
The intention is for this project to be very modular.

Essentially, the engine should be build up of three components.
There's hackersearch itself, in the `hackersearch` directory, which is a website that runs search queries for users.
They way the hackersearch website runs these queries is by first passing them to the module I call TrueQuery.
It splits a piece of text `convert int to string python` into a more complicated object, containing a list of keywords `python`, a subject `programming`, and so on.

Then, when we have the Query object, we have a look at the list of engines.
HackerSearch really consists of several "mini engines".
Currently, the only one that exists is the Stack Overflow MiniEngine `some`.
If the subject of the query object is `programming`, then the query will be passed on to the Stack Overflow engine.
Several engines should be able to register for a subject.

Finally, the results are returned to hackersearch, which presents a nice HTML page to the user.


### Setup

Copy `.env-sample` to `.env` and update accordingly

```sh
cp .env-sample .env
```
