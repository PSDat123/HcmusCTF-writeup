(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-851c22b0"], {
        "65a6": function(e, t, s) {
            "use strict";
            s.r(t);
            var a = function() {
                    var e = this,
                        t = e.$createElement,
                        s = e._self._c || t;
                    return s("div", {
                        staticClass: "chat"
                    }, [s("div", {
                        staticClass: "row"
                    }, [s("div", {
                        staticClass: "flex xs12 md12"
                    }, [s("va-card", {
                        attrs: {
                            title: e.$t("chat.title")
                        }
                    }, [s("chat", {
                        model: {
                            value: e.chatMessages,
                            callback: function(t) {
                                e.chatMessages = t
                            },
                            expression: "chatMessages"
                        }
                    })], 1)], 1)])])
                },
                n = [],
                i = function() {
                    var e = this,
                        t = e.$createElement,
                        s = e._self._c || t;
                    return s("div", {
                        staticClass: "va-chat"
                    }, [s("div", {
                        directives: [{
                            name: "sticky-scroll",
                            rawName: "v-sticky-scroll",
                            value: {
                                animate: !0,
                                duration: 500
                            },
                            expression: "{\n      animate: true,\n      duration: 500\n    }"
                        }],
                        staticClass: "va-chat__body",
                        style: {
                            height: e.height
                        }
                    }, e._l(e.value, (function(t, a) {
                        return s("div", {
                            key: a,
                            staticClass: "va-chat__message",
                            class: {
                                "va-chat__message--yours": t.yours
                            },
                            style: {
                                backgroundColor: t.yours ? e.$themes.primary : void 0
                            }
                        }, [s("span", {
                            staticClass: "va-chat__message-text"
                        }, [e._v(" " + e._s(t.text) + " ")])])
                    })), 0), s("div", {
                        staticClass: "va-chat__controls"
                    }, [s("va-input", {
                        staticClass: "va-chat__input",
                        attrs: {
                            placeholder: "Type your message..."
                        },
                        on: {
                            keypress: function(t) {
                                return !t.type.indexOf("key") && e._k(t.keyCode, "enter", 13, t.key, "Enter") ? null : e.sendMessage(t)
                            }
                        },
                        model: {
                            value: e.inputMessage,
                            callback: function(t) {
                                e.inputMessage = t
                            },
                            expression: "inputMessage"
                        }
                    }), s("va-button", {
                        on: {
                            click: function(t) {
                                return e.sendMessage()
                            }
                        }
                    }, [e._v(" Send ")])], 1)])
                },
                c = [],
                l = s("8800"),
                r = {
                    name: "chat",
                    directives: {
                        StickyScroll: l["a"]
                    },
                    data: function() {
                        return {
                            inputMessage: "",
                            respMessage: ""
                        }
                    },
                    props: {
                        value: {
                            type: Array,
                            default: function() {
                                return [{
                                    text: "Hello! Welcome to challenge",
                                    yours: !1
                                }, {
                                    text: "Do you need any help?",
                                    yours: !1
                                }]
                            }
                        },
                        height: {
                            default: "20rem",
                            type: String
                        }
                    },
                    methods: {
                        sendMessage: function() {
                            this.inputMessage && (this.inputMessage.indexOf("flag") > -1 ? this.respMessage = "HCMUS{w0w_4uth3ntication_bYP4ss_s000_h4rd}" : this.respMessage = "Do you need any help?", this.$emit("input", this.value.concat({
                                text: this.inputMessage,
                                yours: !0
                            }, {
                                text: this.respMessage,
                                yours: !1
                            })), this.inputMessage = "", this.respMessage = "")
                        }
                    }
                },
                u = r,
                o = (s("ab28"), s("2877")),
                h = Object(o["a"])(u, i, c, !1, null, null, null),
                p = h.exports,
                d = {
                    name: "chat-page",
                    components: {
                        Chat: p
                    },
                    data: function() {
                        return {
                            chatMessages: [{
                                text: "Hello! Welcome to challenge",
                                yours: !1
                            }, {
                                text: "Do you need any help?",
                                yours: !1
                            }]
                        }
                    }
                },
                g = d,
                v = Object(o["a"])(g, a, n, !1, null, null, null);
            t["default"] = v.exports
        },
        ab28: function(e, t, s) {
            "use strict";
            var a = s("bec2"),
                n = s.n(a);
            n.a
        },
        bec2: function(e, t, s) {}
    }
]);
//# sourceMappingURL=chunk-851c22b0.e53301b2.js.map