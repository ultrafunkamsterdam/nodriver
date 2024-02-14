# NODRIVER

**This package provides next level webscraping and browser automation
using a relatively simple interface.**

* **This is the official successor of the** [Undetected-Chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver/) **python package.**
* **No more webdriver, no more selenium**

Direct communication provides even better resistance against web applicatinon firewalls (WAF’s), while
performance gets a massive boost.
This module is, contrary to undetected-chromedriver, fully asynchronous.

What makes this package different from other known packages,
is the optimization to stay undetected for most anti-bot solutions.

Another focus point is usability and quick prototyping, so expect a lot to work `-as is-` ,
with most method parameters having `best practice` defaults.
Using 1 or 2 lines, this is up and running, providing best practice config
by default.

While usability and convenience is important. It’s also easy
to fully customizable everything using the entire array of
[CDP](https://chromedevtools.github.io/devtools-protocol/) domains, methods and events available.

## Some features

* A blazing fast undetected chrome (-ish) automation library
* No chromedriver binary or Selenium dependency
* This equals bizarre performance increase and less detections!
* Up and running in 1 line of code\*
* uses fresh profile on each run, cleans up on exit
* save and load cookies to file to not repeat tedious login steps
* fast element lookup, by selector or text. also searches embedded iframes.
* descriptive \_\_repr_\_ for elements, which represent the element as html
* packed with helpers and utility methods for most used and important operations

<!-- * ```elem.text```
* ```elem.text_all```

* ```elem.parent.parent.parent.attrs```
* ```anchor_elem.href and anchor_elem['href']```
* ```anchor_elem.href = 'someotherthing'; await anchor_elem.save()```
* ```elem.children[-1].children[0].children[4]```

* ```await html5video_element.record_video()```
* ```await html5video_element('method')```
* ```await html5video_element.apply('''(el) => el.currentTime = 0''')```
* ```tab = await browser.get(url, new_tab=True)```
* ```tab_win = await browser.get(url, new_window=True)```
* ```first = await tab.find('search text')```
* ```all_results = await tab.find_all('search text')```
* ```first_submit_button = await tab.find(selector='button[type=submit]')```
* ```inputs_in_form = await tab.find_all('form input')``` -->

### Installation

Since it’s a part of undetected-chromedriver, installation goes via

```default
pip install undetected-chromedriver
```

---

<a id="getting-started-commands"></a>

### usage example

The aim of this project (just like undetected-chromedriver, somewhere long ago)
is to keep it short and simple, so you can quickly open an editor or interactive session,
type or paste a few lines and off you go.

```python
import asyncio
import nodriver as uc

async def main():
    browser = await uc.start()
    page = await browser.get('https://www.nowsecure.nl')

    await page.save_screenshot()
    await page.get_content()
    await page.scroll_down(150)
    elems = await page.query_selector_all('*[src]')
    for elem in elems:
        await elem.highlight_position()

    page2 = await browser.get('https://twitter.com', new_tab=True)
    page3 = await browser.get('https://pornhub.com', new_window=True)

    for p in (page, page2, page3):
       await p.bring_to_front()
       await p.scroll_down(200)
       await p.sleep(1)
       await p.reload()
       if p != page3:
           await p.close()


if __name__ == '__main__':

    # since asyncio.run never worked (for me)
    uc.loop().run_until_complete(main())
```

### getting started

* [Installation](nodriver/quickstart.md)
* [usage example](nodriver/quickstart.md#usage-example)
* [Components and interaction](nodriver/quickstart.md#components-and-interaction)

### nodriver object reference

* [Browser class](nodriver/classes/browser.md)
* [Element class](nodriver/classes/element.md)
* [Other classes and Helper classes](nodriver/classes/others_and_helpers.md)
* [`Tab`](nodriver/classes/tab.md)

### nodriver cdp reference

* [Accessibility](nodriver/cdp/accessibility.md)
* [Animation](nodriver/cdp/animation.md)
* [Audits](nodriver/cdp/audits.md)
* [Autofill](nodriver/cdp/autofill.md)
* [BackgroundService](nodriver/cdp/background_service.md)
* [Browser](nodriver/cdp/browser.md)
* [CacheStorage](nodriver/cdp/cache_storage.md)
* [Cast](nodriver/cdp/cast.md)
* [Console](nodriver/cdp/console.md)
* [CSS](nodriver/cdp/css.md)
* [Database](nodriver/cdp/database.md)
* [Debugger](nodriver/cdp/debugger.md)
* [DeviceAccess](nodriver/cdp/device_access.md)
* [DeviceOrientation](nodriver/cdp/device_orientation.md)
* [DOM](nodriver/cdp/dom.md)
* [DOMDebugger](nodriver/cdp/dom_debugger.md)
* [DOMSnapshot](nodriver/cdp/dom_snapshot.md)
* [DOMStorage](nodriver/cdp/dom_storage.md)
* [Emulation](nodriver/cdp/emulation.md)
* [EventBreakpoints](nodriver/cdp/event_breakpoints.md)
* [FedCm](nodriver/cdp/fed_cm.md)
* [Fetch](nodriver/cdp/fetch.md)
* [HeadlessExperimental](nodriver/cdp/headless_experimental.md)
* [HeapProfiler](nodriver/cdp/heap_profiler.md)
* [IndexedDB](nodriver/cdp/indexed_db.md)
* [Input](nodriver/cdp/input_.md)
* [Inspector](nodriver/cdp/inspector.md)
* [IO](nodriver/cdp/io.md)
* [LayerTree](nodriver/cdp/layer_tree.md)
* [Log](nodriver/cdp/log.md)
* [Media](nodriver/cdp/media.md)
* [Memory](nodriver/cdp/memory.md)
* [Network](nodriver/cdp/network.md)
* [Overlay](nodriver/cdp/overlay.md)
* [Page](nodriver/cdp/page.md)
* [Performance](nodriver/cdp/performance.md)
* [PerformanceTimeline](nodriver/cdp/performance_timeline.md)
* [Preload](nodriver/cdp/preload.md)
* [Profiler](nodriver/cdp/profiler.md)
* [Runtime](nodriver/cdp/runtime.md)
* [Schema](nodriver/cdp/schema.md)
* [Security](nodriver/cdp/security.md)
* [ServiceWorker](nodriver/cdp/service_worker.md)
* [Storage](nodriver/cdp/storage.md)
* [SystemInfo](nodriver/cdp/system_info.md)
* [Target](nodriver/cdp/target.md)
* [Tethering](nodriver/cdp/tethering.md)
* [Tracing](nodriver/cdp/tracing.md)
* [WebAudio](nodriver/cdp/web_audio.md)
* [WebAuthn](nodriver/cdp/web_authn.md)
