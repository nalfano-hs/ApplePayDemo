# Apple Pay Demo Script

## Summary:
This script is meant to demonstrate the usage of the Images plugin to interact with the Assistive Touch menu on iOS. Since the Assistive Touch menu is unable to be interacted with through standard element identifiers the most common way to send interactions to it was via sending taps to specific coordinates. This was functional but was also dependent on the assistive touch menu being in the same location every time. By using the Images plugin to find the elements by image you are able to eliminate the need for any hard coded coordinates in your script.

## Appium Requirements:
This script will require an Appium Server that is running a version of Appium 2+ as well as the Images plugin to be installed.

## Device Setup:
This script does require the device to be configured in a specific way for it to function as expected. Please find a list of settings that need to be changed below.

 - Sign into an Apple account with an Apple wallet that has at least one card in it.
 - Navigate to Settings > Accessibility > Touch > AssistiveTouch and turn on AssistiveTouch
    - Scroll to the bottom of the Assistive touch page and turn on "Confirm with AssistiveTouch". Follow the prompts that appear (this will require you to double press the power button to complete)
    - In the AssistiveTouch menu select "Customize Top Level Menu" and select any icon and change it to the Apple Pay icon. This script assumes the Apple Pay icon is on the top level but if you are building your own script this may not be necessary but you will likely need to add more steps to navigate to the default location of that button.
    - Back on the main AssistiveTouch menu you will also want to set the "Idle Opacity" to 100%, this will make it easier to match the image. 

## Images Plugin
This script uses two specific settings from the [Images plugin](https://github.com/appium/appium/blob/master/packages/images-plugin/docs/find-by-image.md), which are set using `driver.update_settings` but these can also be set via the capabilities if you are using Appium 2.1+ by using the [Settings API](https://appium.io/docs/en/2.0/guides/settings/). The first setting that is used is the "imageMatchThreshold" setting which allows you to adjust the sensitivity for how strict the matching is. The second setting used is "fixImageTemplateScale" which will scale the image you provide to match the screenshot that it is trying to match to. This can be helpful depending on the method you are using to obtain your images. Another setting that can be helpful if find by image is sending a click to the wrong location is the "getMatchedImageResult" setting. This setting is used for debugging when writing your script, this will allow you to return an image of the device screen with a highlighted box indicating where it is matching. 

When writing scripts for devices on the Headspin platform it is recommended that you use the screenshot function in the UI to obtain your images. This can be done by manually connecting to a device navigating to where the image you want to interact with is on the device. Then select the Screenshot tab on the right side of the screen, click "Take HQ Screenshot" and download the image. Once it is downloaded, crop it to just take the specific image you need. I found that this will provide a more standard image scale allowing for better matching results.

There is also a two part guide ([part1](https://appiumpro.com/editions/32-finding-elements-by-image-part-1), [part2](https://appiumpro.com/editions/33-finding-elements-by-image-part-2)) on finding elements by images in the Appium Pro newsletter that is a good read, though do note that this was written for an older version of Appium so there may be some syntax differences in the code snippets. 
