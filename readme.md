<div align="center">
<h1>Rovio Activation Script</h1>
  
A collection of scripts that allow you to fully unlock Bad Piggies on your PC.

[Fiddler Script (v1.3.0+)](#fiddler-script) •
[How does it work?](#how-does-it-work) •
[How to use it?](#how-to-use-it) •
[Python Script (all versions)](#python-script) •
[I have a question!](#i-have-a-question)
</div>

---

### Fiddler Script
The Fiddler script works for Bad Piggies 1.3.0+
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

### You can find a version of this script with instructions for Linux (wine) [here](https://github.com/PRO100KatYT/RovioActivationScript/issues/1) thanks to [j-romchain](https://github.com/j-romchain)

---

### How does it work?
In February 2024, the activation servers for full versions of several Rovio PC games, including Bad Piggies, were permanently shut down. When you attempt to enter an activation code in the game’s activation window, the game still sends a request to the servers. However, due to the lack of response from the servers, the activation process fails.

This is where this script comes into play. The script intercepts requests to `cloud.rovio.com/drm/consumeKey/` URL, simulating a server response. It then forwards this simulated response to the game client. As a result, the game believes that the Rovio servers are operational, and the activation code you input is considered valid. Consequently, the game gets activated, allowing you to enjoy the full experience!

#### Without the script:

![bp-activated-no](https://github.com/PRO100KatYT/RovioActivationScript/assets/67335438/ab114f8e-f49e-4092-9dc5-1ec2092ca8d5)

#### With the script:

![bp-activated-yes](https://github.com/PRO100KatYT/RovioActivationScript/assets/67335438/31f55c2d-a198-4c51-9cef-0f6297788955)

### How to use it?
- Download and Install [Fiddler Classic](https://www.telerik.com/download/fiddler) and open it.

- If you get an `AppContainer Configuration` popup, click cancel.

- Head to the `FiddlerScript` section.

- If there is an Introduction script, remove it.

- Paste [the script](#fiddler-script) there and click on `Save Script`.

- Go to Bad Piggies and input any code into the activation window and confirm it.

- Your Bad Piggies PC copy should be activated. You can now close Fiddler and play the game!
---


### Python Script

As an alternative to the Fiddler method, you can use the Rovio Actvation Python script. This script automatically generates the necessary configuration `Settings.xml` file with the activation data and saves it in the game data folder in AppData. This method works for all Bad Piggies versions on Windows.

### How to use the Python script:

- Download and extract the RovioActivationScript.py file to any location on your Windows PC from this repository. [(Direct download link)](https://github.com/PRO100KatYT/RovioActivationScript/archive/refs/heads/main.zip)
- Make sure you have [Python](https://www.python.org/downloads/) installed (tested on version 3.9 but should work on 3.2 or newer).
- Close the game if it's open.
- Run the downloaded script (e.g., by double-clicking it).
- Once the script is finished with no errors, Bad Piggies should be activated!

---

### I have a question!
Feel free to [open an issue](https://github.com/PRO100KatYT/RovioActivationScript/issues/new "Click here if you want to open an issue.") and ask your question there.
