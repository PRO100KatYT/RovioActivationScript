<div align="center">
<h1>Rovio Activation Script</h1>
  
A Fiddler script that allows you to fully unlock Bad Piggies via the activation window in the main menu of the game on PC.

[The Script](#the-script) •
[How does it work?](#how-does-it-work) •
[How to use it?](#how-to-use-it) •
[I have a question!](#i-have-a-question)
</div>

---

### The Script
```javascript
import Fiddler;
// Script by PRO100KatYT
 
class Handlers
{
    static function OnBeforeRequest(oSession: Session) {
        if (oSession.fullUrl.Contains("cloud.rovio.com/drm/consumeKey/"))
        {
            oSession.utilCreateResponseAndBypassServer();
            oSession.responseCode = 200;
            oSession.oResponse.headers.HTTPResponseCode = 200;
            oSession.oResponse.headers.HTTPResponseStatus = "200 OK";
            oSession.utilSetResponseBody("status=1&msg=valid");
        }
    }
}
```

---

### How does it work?
In February 2024, the activation servers for full versions of several Rovio PC games, including Bad Piggies, were permanently shut down. When you attempt to enter an activation code in the game’s activation window, the game still sends a request to the servers. However, due to the lack of response from the servers, the activation process fails.

This is where this script comes into play. The script intercepts requests to `cloud.rovio.com/drm/consumeKey/` URL, simulating a server response. It then forwards this simulated response to the game client. As a result, the game believes that the Rovio servers are operational, and the activation code you input is considered valid. Consequently, the game gets activated, allowing you to enjoy the full experience!

#### Without the script:

![bp-activated-no](https://github.com/PRO100KatYT/RovioActivationScript/assets/67335438/ab114f8e-f49e-4092-9dc5-1ec2092ca8d5)

#### With the script:

![bp-activated-yes](https://github.com/PRO100KatYT/RovioActivationScript/assets/67335438/31f55c2d-a198-4c51-9cef-0f6297788955)

---

### How to use it?
- Download and Install [Fiddler Classic](https://www.telerik.com/download/fiddler) and open it.

- If you get an `AppContainer Configuration` popup, click cancel.

- Head to the `FiddlerScript` section.

- If there is an Introduction script, remove it.

- Paste [the script](#the-script) there and click on `Save Script`.

- Go to Bad Piggies and input any code into the activation window and confirm it.

- Now your Bad Piggies PC copy should be activated.
---

### I have a question!
Feel free to [open an issue](https://github.com/PRO100KatYT/RovioActivationScript/issues/new "Click here if you want to open an issue.") and ask your question there.
