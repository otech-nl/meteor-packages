# Meteor overview and major packages

This repository contains a brief overview of (http://meteor.com)[Meteor] and an list of its major packages.

## Overview

The following features distinguish Meteor from other web-platforms:
<dl>
    <dt>data over the wire</dt><dd>In Meteor client and server exchange data, not HTML.
    <dl>
        <dt>single page app (SPA)</dt><dd>This means that the client is loaded as a whole at start-up and then manages the user interaction without unnecessary calls to the server. This makes for a smooth user-experience.</dd>
        <dt>no REST</dt><dd>As you can access data from the client just as you would from the server, data over the wire also means that there is not need for REST interfaces.</dd>
    </dl>
    </dd>
    <dt>full-stack</dt><dd>In Meteor the functionality on both the server (through node.js) and the client (through the browser) is implemented in Javascript (ES2015+ to be exact). This saves the developer from continuously having to switch between languages.</dd>
    <dt>multi-platform</dt><dd>With Meteor you can build apps for web, iOS, and Android from the samen code base. Nou mar nerd Cordova for platform-specific features.</dd>
    <dt>no SQL</dt><dd>Meteor uses Mongodb as its data backend. Mongodb is document-based and does not use SQL.</dd>
    <dt>reactivity</dt><dd>Data in Meteor is updated everywhere once it changes. This includes all active clients, which adds to the smooth user-experience.</dd>
</dl>

The mindmap below shows how I understand Meteor:

![Meteor mindmap](Meteor.png)

The client handles routing and rendering. Routing is taken care of by Flow router, which uses Blaze as template engine (Angular and React are also supported). Templates are divided in three layers:

- layouts define the general structure of your site, using pages
- pages are smart, which means they collect data and feed them to components
- components do not interact with anything except though parameters, which makes them highly reusable

Templates can be controlled through helpers and event handlers (including onCreated).

The server uses Mongodb as a datastore. Data is stored in collections, which are basically persistent JSON documents. A schema language is used to define the datastructures, so data can be validated. Schema also drive the autoform package. Collections can be controlled through helpers and hooks.

The client and server communicate through a publish/subscribe mechanism and through methods. The server controls data access by selectively publishing data to the client. The client (pages) collect data through subscriptions. Methods are Meteor's remote procedure calls (RPCs) and can use schema for data validation.

Some final tips & tricks:

- <tt>waitOn</tt> (package Iron Router) lets you defer execution untill a subscription has finished
- Meteor methods <i>can</i> be called synchronously on the server, but <i>must</i> be called asynchronously  on the client
- Global variables aren't available from templates. Access them with template helper.
- add <tt>c:\Windows\System32</tt> to path on tasklist.exe error
- The autorun function lets you define a function that is run automatically when a reactive data source changes.



## Packages

Just like all other modern frameworks, Meteor relies heavily on third party packages from its thriving eco-system. The Meteor [Guide](http://guide.meteor.com) gives an opinionated overview of which packages to use. The table below shows these packages in the middle column, along with some additional packages I prefer in the final column. For more packages visit [Atmosphere js](https://atmospherejs.com/packages/most-used). You can import all these package definitions by importing the file <tt>packages</tt> from this repository into the file <tt>packages</tt> of your project and the remove any package you don't need.

<table id="packages">
<tr><th>subject</th><th>guide</th><th>extra</th></tr>

<tr><td>Out of the box</td><td>

- [http](https://docs.meteor.com/api/http.html)
- [jQuery](https://docs.meteor.com/packages/jquery.html)
- [markdown](https://docs.meteor.com/packages/markdown.html)
- [meteor:ecmascript](http://atmospherejs.com/meteor/ecmascript)
- [underscore](https://docs.meteor.com/packages/underscore.html)
</td><td>
</td>
</tr>
<tr><td>Collections</td><td>

- [aldeed:collection2](http://atmospherejs.com/aldeed/collection2)
- [aldeed:simple-schema](http://atmospherejs.com/aldeed/simple-schema) (or [jagi:astronomy](http://atmospherejs.com/jagi/astronomy))
- [dburles:collection-helpers](http://atmospherejs.com/dburles/collection-helpers)
- [percolate:migrations](http://atmospherejs.com/percolate/migrations)
</td><td>
</td>
</tr>
<tr><td>Data-loading</td><td>

- [percolate:find-from-publication](http://atmospherejs.com/percolate/find-from-publication)
- [reywood:publish-composite](http://atmospherejs.com/reywood/publish-composite)
- [simple:rest](http://atmospherejs.com/simple/rest)
- [tmeasday:publish-counts](http://atmospherejs.com/tmeasday/publish-counts)
</td><td>
</td></tr>
<tr><td>Methods</td><td>

- [mdg:validated-method](https://atmospherejs.com/mdg/validated-method)
</td><td>
</td></tr>
<tr><td>User accounts</td><td>

- [alanning:roles](http://atmospherejs.com/alanning/roles)
- [arillo:flow-router-helpers](http://atmospherejs.com/arillo/flow-router-helpers)
- [useraccounts:flow-routing](http://atmospherejs.com/useraccounts/flow-routing)
- [useraccounts:core](http://atmospherejs.com/useraccounts/core)
- [useraccounts:unstyled](http://atmospherejs.com/useraccounts/unstyled)
</td><td>

- [didericis:permissions-mixin](http://atmospherejs.com/didericis/permissions-mixin)
- [matb33:collection-hooks](http://atmospherejs.com/matb33/collection-hooks)
- [ongoworks:security](http://atmospherejs.com/ongoworks/security)
- [ostrio:user-status](http://atmospherejs.com/ostrio/user-status) (or [tmeasday:presence](http://atmospherejs.com/tmeasday/presence))
</td></tr>
<tr><td>Routing</td><td>

- [arillo:flow-router-helpers](http://atmospherejs.com/arillo/flow-router-helpers)
- [kadira:flow-router](http://atmospherejs.com/kadira/flow-router)
- [kadira:blaze-layout](http://atmospherejs.com/kadira/blaze-layout)
- [nimble:restivus](http://atmospherejs.com/nimble/restivus)
- [zimme:active-route](http://atmospherejs.com/zimme/active-route)
</td><td>

- [ostrio:flow-router-extra](http://atmospherejs.com/ostrio/flow-router-extra)
</td></tr>
<tr><td>UI-UX</td><td>

- [aldeed:autoform](http://atmospherejs.com/aldeed/autoform)
- [percolate:momentum](http://atmospherejs.com/percolate/momentum)
- [tap:i18n](http://atmospherejs.com/tap/i18n) (or [universe:18n](http://atmospherejs.com/universe/18n))
</td><td>

- [aldeed:tabular](http://atmospherejs.com/aldeed/tabular) (or )
- [aldeed:template-extension](http://atmospherejs.com/aldeed/template-extension)
- [aslagle:reactive-table](http://atmospherejs.com/aslagle/reactive-table)
- [chrismbeckett:toastr](http://atmospherejs.com/chrismbeckett/toastr)
- [fortawesome:fontawesome](http://atmospherejs.com/fortawesome/fontawesome)
- [matb33:bootstrap-glyphicons](http://atmospherejs.com/matb33:bootstrap-glyphicons)
- [raix:push](http://atmospherejs.com/raix/push)
- [semantic:ui](http://atmospherejs.com/semantic/ui)
- [twbs:bootstrap](http://atmospherejs.com/twbs/bootstrap)
</td></tr>
<tr><td>Other</td><td>
</td><td>

- [dburles:google-maps](http://atmospherejs.com/dburles/google-maps)
- [easy:search](http://atmospherejs.com/easy/search)
- [momentjs:moment](http://atmospherejs.com/momentjs/moment)
- [sach:flow-db-admin](http://atmospherejs.com/sach/flow-db-admin)

</td></tr>
<tr><td>Testing</td><td>

- [dburles:factory](http://atmospherejs.com/dburles/factory)
- [hwillson:stub-collections](http://atmospherejs.com/hwillson/stub-collections)
- [johanbrook:publication-collector](http://atmospherejs.com/johanbrook/publication-collector)
- [meteortesting:mocha](http://atmospherejs.com/meteortesting/mocha)
- [practicalmeteor:mocha](http://atmospherejs.com/practicalmeteor/mocha)
- [velocity:meteor-stubs](http://atmospherejs.com/velocity/meteor-stubs)
- [xolvio:cleaner](http://atmospherejs.com/xolvio/cleaner)
</td><td>

- [Chimp](https://chimp.readme.io/) (not really a package)
</td></tr>
<tr><td>Deployment</td><td>

- [dferber:prerender](http://atmospherejs.com/dferber/prerender)
- [kadira:dochead](http://atmospherejs.com/kadira/dochead)
- [mdg:seo](http://atmospherejs.com/mdg/seo)
- [okgrow:analytics](http://atmospherejs.com/okgrow/analytics)
</td><td>
</td></tr>
</table>
