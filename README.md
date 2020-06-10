# Discogs API Client

This is a Python interface to the Discogs [REST API][0]. It is intended as a drop-in replacement for the now deprecated `discogs-client` ([GitHub][1], [PyPi][2]). Pull requests are welcome!

It enables you to query the Discogs database for information on artists, releases, labels, users, Marketplace listings, and more. It also supports OAuth 1.0a authorization, which allows you to change user data such as profile information, collections and wantlists, inventory, and orders.

[![Build Status](https://travis-ci.org/grawlinson/python-discogs-api.svg?branch=master)](https://travis-ci.org/grawlinson/python-discogs-api)
[![Coverage Status](https://coveralls.io/repos/github/grawlinson/python-discogs-api/badge.svg?branch=master)](https://coveralls.io/github/grawlinson/python-discogs-api?branch=master)

## Installation

Install the client from PyPI using your favorite package manager.

```sh
pip install discogs_api
```

## Quickstart

### Instantiating the client object

```python
>>> import discogs_api
>>> d = discogs_api.Client('ExampleApplication/0.1')
```

### Authorization (optional)

There are a couple of different authorization methods you can choose from depending on your requirements.

#### OAuth authentication

This method will allow your application to make requests on behalf of any user who logs in.

For this, specify your app's consumer key and secret:

```python
>>> d.set_consumer_key('key-here', 'secret-here')
# Or you can do this when you instantiate the Client
```

Then go through the OAuth 1.0a process. In a web app, we'd specify a `callback_url`. In this example, we'll use the OOB flow.

```python
>>> d.get_authorize_url()
('request-token', 'request-secret', 'authorize-url-here')
```

The client will hang on to the access token and secret, but in a web app, you'd want to persist those and pass them into a new `Client` instance on the next request.

Next, visit the authorize URL, authenticate as a Discogs user, and get the verifier:

```python
>>> d.get_access_token('verifier-here')
('access-token-here', 'access-secret-here')
```

Now you can make requests on behalf of the user.

```python
>>> me = d.identity()
>>> "I'm {0} ({1}) from {2}.".format(me.name, me.username, me.location)
u"I'm Joe Bloggs (example) from Portland, Oregon."
>>> len(me.wantlist)
3
>>> me.wantlist.add(d.release(5))
>>> len(me.wantlist)
4
```

#### User-token authentication

This is one of the simplest ways to authenticate and become able to perform requests requiring authentication, such as search (see below). The downside is that you'll be limited to the information only your user account can see (i.e., no requests on behalf of other users).

For this, you'll need to generate a user-token from your developer settings on the Discogs website.

```python
>>> d = discogs_api.Client('ExampleApplication/0.1', user_token="my_user_token")
```

## Fetching data

Use methods on the client to fetch objects. You can search for objects:

```python
>>> results = d.search('Stockholm By Night', type='release')
>>> results.pages
1
>>> artist = results[0].artists[0]
>>> artist.name
u'Persuader, The'
```

Or fetch them by ID:

```python
>>> artist.id
1
>>> artist == d.artist(1)
True
```

You can drill down as far as you like.

```python
>>> releases = d.search('Bit Shifter', type='artist')[0].releases[1].\
...     versions[0].labels[0].releases
>>> len(releases)
134
```

## Artist

Query for an artist using the artist's name:

```python
>>> artist = d.artist(956139)
>>> print artist
<Artist "...">
>>> 'name' in artist.data.keys()
True
```

Get a list of `Artist`s representing this artist's aliases:

```python
>>> artist.aliases
[...]
```

Get a list of `Release`s by this artist by page number:

```python
>>> artist.releases.page(1)
[...]
```

## Release

Query for a release using its Discogs ID:

```python
>>> release = d.release(221824)
```

Get the title of this `Release`:

```python
>>> release.title
u'...'
```

Get a list of all `Artist`s associated with this `Release`:

```python
>>> release.artists
[<Artist "...">]
```

Get the tracklist for this `Release`:

```python
>>> release.tracklist
[...]
```

Get the `MasterRelease` for this `Release`:

```python
>>> release.master
<MasterRelease "...">
```

Get a list of all `Label`s for this `Release`:

```python
>>> release.labels
[...]
```

## MasterRelease

Query for a master release using its Discogs ID:

```python
>>> master_release = d.master(120735)
```

Get the key `Release` for this `MasterRelease`:

```python
>>> master_release.main_release
<Release "...">
```

Get the title of this `MasterRelease`:

```python
>>> master_release.title
u'...'
>>> master_release.title == master_release.main_release.title
True
```

Get a list of `Release`s representing other versions of this `MasterRelease` by page number:

```python
>>> master_release.versions.page(1)
[...]
```

Get the tracklist for this `MasterRelease`:

```python
>>> master_release.tracklist
[...]
```

## Label

Query for a label using the label's name:

```python
>>> label = d.label(6170)
```

Get a list of `Release`s from this `Label` by page number:

```python
>>> label.releases.page(1)
[...]
```

Get a list of `Label`s representing sublabels associated with this `Label`:

```python
>>> label.sublabels
[...]
```

Get the `Label`'s parent label, if it exists:

```python
>>> label.parent_label
<Label "Warp Records Limited">
```

[0]: https://www.discogs.com/developers
[1]: https://github.com/discogs/discogs_client
[2]: https://pypi.org/project/discogs-client/

