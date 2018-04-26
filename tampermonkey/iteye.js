// ==UserScript==
// @name         iteye去广告
// @namespace    https://www.ieevee.com
// @version      0.2
// @description  iteye去掉adgard去不掉的广告
// @author       silenceshell
// @match        http://*.iteye.com/blog/*
// @grant        none
// ==/UserScript==

var ad = document.getElementById("nav_show_top_stop");
var adp = ad.parentElement;
var removed = adp.removeChild(ad);

