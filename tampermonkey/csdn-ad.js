// ==UserScript==
// @name         CSDN去广告
// @namespace    https://www.ieevee.com
// @version      0.2
// @description  iteye去掉adgard去不掉的广告
// @author       silenceshell
// @match        https://blog.csdn.net/*/article/details/*
// @grant        none
// ==/UserScript==

var ads = document.getElementsByClassName("box-box-large");
var adp = ads[0].parentElement;
var removed = adp.removeChild(ads[0]);

