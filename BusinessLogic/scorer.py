# from main.py import topsis as tp

labels = ['coffee','tea','shampoo','face serum','bread','honey','soap','biscuit','milk','chocolate','juice']

json= {
    "context": {
        "domain": "nic2004:52110",
        "country": "IND",
        "city": "std:080",
        "action": "search",
        "core_version": "1.1.0",
        "bap_id": "buyer-app-preprod.ondc.org",
        "bap_uri": "https://buyer-app-preprod.ondc.org/protocol/v1",
        "transaction_id": "2bb37678-3a61-48d6-985d-3c33dd2821d9",
        "message_id": "858ebbc0-d54d-459e-ad04-5adc2a88ef21",
        "timestamp": "2024-02-08T05:40:13.781Z",
        "ttl": "PT30S"
    },
    "message": {
        "catalogs": [
            {
                "id": "8901088721004",
                "time": {
                    "label": "enable",
                    "timestamp": "2024-02-08T05:29:14.000Z"
                },
                "parent_item_id": "CAT_55_8901088721004",
                "price": {
                    "currency": "INR",
                    "value": "292.0",
                    "maximum_value": "290"
                },
                "quantity": {
                    "unitized": {
                        "measure": {
                            "unit": "gm",
                            "value": 1
                        }
                    },
                    "available": {
                        "count": "0"
                    },
                    "maximum": {
                        "count": "0"
                    }
                },
                "descriptor": {
                    "name": "Saffola Honey Gold, 100% Pure NMR Tested Honey, Made with Kashmir Honey, 500g",
                    "symbol": "https://marico.com/html/images/favicon.png",
                    "short_desc": "Saffola Honey Gold, 100% Pure NMR Tested Honey, Made with Kashmir Honey, 500g",
                    "long_desc": "Saffola Honey Gold, 100% Pure NMR Tested Honey, Made with Kashmir Honey, 500g",
                    "images": [
                        "https://images.marico.in/assets/saffola/logo.png"
                    ],
                    "code": "1:8901088721004"
                },
                "location_id": "ondcpreprod-marico-in-1",
                "category_id": "Gourmet & World Foods",
                "fulfillment_id": "1",
                "recommended": true,
                "@ondc/org/returnable": false,
                "@ondc/org/seller_pickup_return": false,
                "@ondc/org/return_window": "P7D",
                "@ondc/org/cancellable": false,
                "@ondc/org/available_on_cod": false,
                "@ondc/org/time_to_ship": "P1D",
                "@ondc/org/contact_details_consumer_care": "Saffola,saffolasupport@marico.com,917777007402",
                "@ondc/org/statutory_reqs_packaged_commodities": {
                    "manufacturer_or_packer_name": "Marico Limited",
                    "manufacturer_or_packer_address": "Mumbai Nasik Highway, NH3, Next to Shangrilla resort, Bhoirgaon Village, Mumbai,Maharashtra 421302",
                    "common_or_generic_name_of_commodity": "Saffola",
                    "month_year_of_manufacture_packing_import": "01/2020"
                },
                "@ondc/org/statutory_reqs_prepackaged_food": {
                    "nutritional_info": "Energy (KCal) - (per 100g) 420, (per serving 50g) 250; Protein (g) - (per 100g) 12, (per serving 50g) 6",
                    "additives_info": "Preservatives, Artificial Colors",
                    "brand_owner_FSSAI_license_no": "12345678901234",
                    "other_FSSAI_license_no": "12345678901234",
                    "importer_FSSAI_license_no": "12345678901234"
                },
                "tags": [
                    {
                        "code": "origin",
                        "list": [
                            {
                                "code": "country",
                                "value": "IND"
                            }
                        ]
                    },
                    {
                        "code": "image",
                        "list": [
                            {
                                "code": "type",
                                "value": "back_image"
                            },
                            {
                                "code": "url",
                                "value": ""
                            }
                        ]
                    },
                    {
                        "code": "veg_nonveg",
                        "list": [
                            {
                                "code": "veg",
                                "value": "yes"
                            }
                        ]
                    }
                ],
                "provider_details": {
                    "id": "ondcpreprod.marico.in",
                    "descriptor": {
                        "name": "Marico",
                        "symbol": "https://images.marico.in/assets/saffola/logo.png",
                        "short_desc": "Buy Saffola Online at Best Price in India - Saffola Stores",
                        "long_desc": "Buy Saffola Online at Best Price in India - Saffola Stores",
                        "images": [
                            "https://images.marico.in/assets/saffola/logo.png"
                        ]
                    }
                },
                "location_details": {
                    "id": "ondcpreprod-marico-in-1",
                    "gps": "19.346264481569786,73.13839363180752",
                    "address": {
                        "locality": "Mumbai Nasik Highway, NH3, Next to Shangrilla resort, Bhoirgaon Village",
                        "street": "Mumbai Nasik Highway, NH3, Next to Shangrilla resort, Bhoirgaon Village",
                        "city": "Mumbai",
                        "state": "Maharashtra",
                        "area_code": "421302"
                    },
                    "time": {
                        "label": "open",
                        "timestamp": "2024-02-08T05:40:05.525Z",
                        "range": {
                            "start": "0000",
                            "end": "2359"
                        },
                        "days": "1,2,3,4,5,6,7",
                        "schedule": {
                            "holidays": []
                        }
                    }
                },
                "category_details": {},
                "fulfillment_details": {
                    "id": "1",
                    "type": "Delivery"
                },
                "context": {
                    "domain": "nic2004:52110",
                    "country": "IND",
                    "city": "std:080",
                    "action": "on_search",
                    "core_version": "1.1.0",
                    "bap_id": "buyer-app-preprod.ondc.org",
                    "bap_uri": "https://buyer-app-preprod.ondc.org/protocol/v1",
                    "bpp_id": "ondcpreprod.marico.in",
                    "bpp_uri": "https://ondcpreprod.marico.in/retail/",
                    "transaction_id": "c4e9650a-860e-47b0-b773-d3a5213ef52d",
                    "message_id": "858ebbc0-d54d-459e-ad04-5adc2a88ef21",
                    "timestamp": "2024-02-08T05:40:05.585Z",
                    "ttl": "PT24H"
                },
                "bpp_details": {
                    "name": "Marico",
                    "symbol": "https://images.marico.in/assets/saffola/logo.png",
                    "short_desc": "Buy Saffola Online at Best Price in India - Saffola Stores",
                    "long_desc": "Buy Saffola Online at Best Price in India - Saffola Stores",
                    "images": [
                        "https://images.marico.in/assets/saffola/logo.png"
                    ],
                    "bpp_id": "ondcpreprod.marico.in"
                },
                "storeOpenTillDate": "2024-02-08T23:59:00.773Z"
            },
            {
                "id": "DFFMCHARMASK01",
                "time": {
                    "label": "enable",
                    "timestamp": "2024-02-08T05:40:05.277Z"
                },
                "descriptor": {
                    "name": "Dermafique Bio Cellulose Charcoal Face Serum Sheet Mask with honey, chamomile, green tea extracts, with Salicylic Acid, Hyaluronic Acid. Made Bio-degradable fibres, Paraben Free, Dermatologist tested",
                    "code": "1:8905110000440",
                    "symbol": "http://admin.itcstore.in/media/catalog/product/s/k/sku_44.png",
                    "short_desc": "Dermafique Bio Cellulose Charcoal Face Serum Sheet Mask with honey, chamomile, green tea extracts, with Salicylic Acid, Hyaluronic Acid. Made Bio-degradable fibres, Paraben Free, Dermatologist tested",
                    "long_desc": "Dermafique Bio Cellulose Charcoal Face Serum Sheet Mask with honey, chamomile, green tea extracts, with Salicylic Acid, Hyaluronic Acid. Made Bio-degradable fibres, Paraben Free, Dermatologist tested",
                    "images": [
                        "http://admin.itcstore.in/media/catalog/product/s/k/sku_44.png",
                        "http://admin.itcstore.in/media/catalog/product/d/e/dermafique-9.png",
                        "http://admin.itcstore.in/media/catalog/product/q/h/qhmqgib9.png",
                        "http://admin.itcstore.in/media/catalog/product/n/3/n3hyc4j1.png",
                        "http://admin.itcstore.in/media/catalog/product/6/2/62fn2fjs.png",
                        "http://admin.itcstore.in/media/catalog/product/0/s/0sorwuat.png",
                        "http://admin.itcstore.in/media/catalog/product/1/d/1dg5nisa.png"
                    ]
                },
                "quantity": {
                    "unitized": {
                        "measure": {
                            "unit": "gram",
                            "value": "10"
                        }
                    },
                    "available": {
                        "count": "99"
                    },
                    "maximum": {
                        "count": "5"
                    }
                },
                "price": {
                    "currency": "INR",
                    "value": "314.0",
                    "maximum_value": "349"
                },
                "category_id": "Beauty & Hygiene",
                "fulfillment_id": "1",
                "location_id": "ONDC-STORE-BGLR",
                "@ondc/org/returnable": true,
                "@ondc/org/cancellable": true,
                "@ondc/org/return_window": "P2D",
                "@ondc/org/seller_pickup_return": false,
                "@ondc/org/time_to_ship": "P1D",
                "@ondc/org/available_on_cod": false,
                "@ondc/org/contact_details_consumer_care": "Support Agent,support@itcstore.in,18003098994",
                "tags": [
                    {
                        "code": "origin",
                        "list": [
                            {
                                "code": "country",
                                "value": "IND"
                            }
                        ]
                    },
                    {
                        "code": "image",
                        "list": [
                            {
                                "code": "type",
                                "value": "back_image"
                            },
                            {
                                "code": "url",
                                "value": "http://admin.itcstore.in/media/catalog/product/s/k/sku_44.png"
                            }
                        ]
                    },
                    {
                        "code": "veg_nonveg",
                        "list": [
                            {
                                "code": "veg",
                                "value": "yes"
                            }
                        ]
                    }
                ],
                "@ondc/org/statutory_reqs_prepackaged_food": {
                    "nutritional_info": "Yes",
                    "additives_info": "Yes",
                    "brand_owner_FSSAI_license_no": "11220303000336",
                    "other_FSSAI_license_no": "11220303000336",
                    "importer_FSSAI_license_no": "11220303000336",
                    "imported_product_country_of_origin": "IND"
                },
                "provider_details": {
                    "id": "ONDC-STORE-BGLR",
                    "descriptor": {
                        "name": "ITC Store",
                        "symbol": "https://retailconnect.co.in/ONDC/itc-cart-1.png",
                        "short_desc": "ITC Store",
                        "long_desc": "ITC Store",
                        "images": [
                            "https://retailconnect.co.in/ONDC/itc-cart-1.png"
                        ]
                    }
                },
                "location_details": {
                    "id": "ONDC-STORE-BGLR",
                    "gps": "12.8389239,77.6860114",
                    "address": {
                        "street": "Warehouse Building N, Khata No.2605/115and2606/114, Kammasandra Village, Anekal Taluk, Attibele Hobli",
                        "locality": "Kammasandra Village, Anekal Taluk, Attibele Hobli",
                        "city": "Bangalore",
                        "area_code": "560067",
                        "state": "KA"
                    },
                    "circle": {
                        "gps": "12.8389239,77.6860114",
                        "radius": {
                            "unit": "km",
                            "value": "50"
                        }
                    },
                    "time": {
                        "label": "enable",
                        "timestamp": "2024-02-08T05:40:05.277Z",
                        "days": "1,2,3,4,5,6,7",
                        "schedule": {
                            "holidays": []
                        },
                        "range": {
                            "start": "0700",
                            "end": "2300"
                        }
                    }
                },
                "category_details": {},
                "fulfillment_details": {
                    "id": "1",
                    "type": "Delivery"
                },
                "context": {
                    "domain": "nic2004:52110",
                    "country": "IND",
                    "city": "std:080",
                    "action": "on_search",
                    "core_version": "1.2.0",
                    "bap_id": "buyer-app-preprod.ondc.org",
                    "bap_uri": "https://buyer-app-preprod.ondc.org/protocol/v1",
                    "bpp_id": "retailconnect.co.in",
                    "bpp_uri": "https://retailconnect.co.in/ondc/public/OndcPreProd/callback",
                    "transaction_id": "c4e9650a-860e-47b0-b773-d3a5213ef52d",
                    "message_id": "858ebbc0-d54d-459e-ad04-5adc2a88ef21",
                    "timestamp": "2024-02-08T05:40:05.277Z"
                },
                "bpp_details": {
                    "name": "ITC Store",
                    "symbol": "https://retailconnect.co.in/ONDC/itc-cart-1.png",
                    "short_desc": "Online eCommerce Store",
                    "long_desc": "Online eCommerce Store",
                    "images": [
                        "https://retailconnect.co.in/ONDC/itc-cart-1.png"
                    ],
                    "tags": [
                        {
                            "code": "bpp_terms",
                            "list": [
                                {
                                    "code": "np_type",
                                    "value": "ISN"
                                }
                            ]
                        }
                    ],
                    "bpp_id": "retailconnect.co.in"
                },
                "storeOpenTillDate": "2024-02-08T23:00:00.774Z"
            },
            {
                "id": "SBREDHONEYCOFEE100",
                "time": {
                    "label": "enable",
                    "timestamp": "2024-02-08T05:40:05.277Z"
                },
                "descriptor": {
                    "name": "Sunbean Red Honey Coffee 100G",
                    "code": "1:8901725115548",
                    "symbol": "http://admin.itcstore.in/media/catalog/product/s/k/sku_557.png",
                    "short_desc": "Sunbean Red Honey Coffee 100G",
                    "long_desc": "Sunbean Red Honey Coffee 100G",
                    "images": [
                        "http://admin.itcstore.in/media/catalog/product/s/k/sku_557.png",
                        "http://admin.itcstore.in/media/catalog/product/i/t/itc_53144_gourmetnewblendvariantsmockup.jpg",
                        "http://admin.itcstore.in/media/catalog/product/1/_/1_6990b207-c681-498c-a668-a90bfaff77ea.jpg",
                        "http://admin.itcstore.in/media/catalog/product/2/_/2_3f0434a1-cc4b-4ba1-8349-d82e54e66d0f.jpg",
                        "http://admin.itcstore.in/media/catalog/product/3/_/3_2d01d2f3-7179-4954-b975-322ddb7bc57d.jpg",
                        "http://admin.itcstore.in/media/catalog/product/4/_/4_60572cec-3008-469a-bf48-24f07aee8444.jpg"
                    ]
                },
                "quantity": {
                    "unitized": {
                        "measure": {
                            "unit": "gram",
                            "value": "100"
                        }
                    },
                    "available": {
                        "count": "0"
                    },
                    "maximum": {
                        "count": "5"
                    }
                },
                "price": {
                    "currency": "INR",
                    "value": "300.0",
                    "maximum_value": "300"
                },
                "category_id": "Tea and Coffee",
                "fulfillment_id": "1",
                "location_id": "ONDC-STORE-BGLR",
                "@ondc/org/returnable": true,
                "@ondc/org/cancellable": true,
                "@ondc/org/return_window": "P2D",
                "@ondc/org/seller_pickup_return": false,
                "@ondc/org/time_to_ship": "P1D",
                "@ondc/org/available_on_cod": false,
                "@ondc/org/contact_details_consumer_care": "Support Agent,support@itcstore.in,18003098994",
                "tags": [
                    {
                        "code": "origin",
                        "list": [
                            {
                                "code": "country",
                                "value": "IND"
                            }
                        ]
                    },
                    {
                        "code": "image",
                        "list": [
                            {
                                "code": "type",
                                "value": "back_image"
                            },
                            {
                                "code": "url",
                                "value": "http://admin.itcstore.in/media/catalog/product/s/k/sku_557.png"
                            }
                        ]
                    },
                    {
                        "code": "veg_nonveg",
                        "list": [
                            {
                                "code": "veg",
                                "value": "yes"
                            }
                        ]
                    }
                ],
                "@ondc/org/statutory_reqs_prepackaged_food": {
                    "nutritional_info": "Yes",
                    "additives_info": "Yes",
                    "brand_owner_FSSAI_license_no": "11220303000336",
                    "other_FSSAI_license_no": "11220303000336",
                    "importer_FSSAI_license_no": "11220303000336",
                    "imported_product_country_of_origin": "IND"
                },
                "provider_details": {
                    "id": "ONDC-STORE-BGLR",
                    "descriptor": {
                        "name": "ITC Store",
                        "symbol": "https://retailconnect.co.in/ONDC/itc-cart-1.png",
                        "short_desc": "ITC Store",
                        "long_desc": "ITC Store",
                        "images": [
                            "https://retailconnect.co.in/ONDC/itc-cart-1.png"
                        ]
                    }
                },
                "location_details": {
                    "id": "ONDC-STORE-BGLR",
                    "gps": "12.8389239,77.6860114",
                    "address": {
                        "street": "Warehouse Building N, Khata No.2605/115and2606/114, Kammasandra Village, Anekal Taluk, Attibele Hobli",
                        "locality": "Kammasandra Village, Anekal Taluk, Attibele Hobli",
                        "city": "Bangalore",
                        "area_code": "560067",
                        "state": "KA"
                    },
                    "circle": {
                        "gps": "12.8389239,77.6860114",
                        "radius": {
                            "unit": "km",
                            "value": "50"
                        }
                    },
                    "time": {
                        "label": "enable",
                        "timestamp": "2024-02-08T05:40:05.277Z",
                        "days": "1,2,3,4,5,6,7",
                        "schedule": {
                            "holidays": []
                        },
                        "range": {
                            "start": "0700",
                            "end": "2300"
                        }
                    }
                },
                "category_details": {},
                "fulfillment_details": {
                    "id": "1",
                    "type": "Delivery"
                },
                "context": {
                    "domain": "nic2004:52110",
                    "country": "IND",
                    "city": "std:080",
                    "action": "on_search",
                    "core_version": "1.2.0",
                    "bap_id": "buyer-app-preprod.ondc.org",
                    "bap_uri": "https://buyer-app-preprod.ondc.org/protocol/v1",
                    "bpp_id": "retailconnect.co.in",
                    "bpp_uri": "https://retailconnect.co.in/ondc/public/OndcPreProd/callback",
                    "transaction_id": "c4e9650a-860e-47b0-b773-d3a5213ef52d",
                    "message_id": "858ebbc0-d54d-459e-ad04-5adc2a88ef21",
                    "timestamp": "2024-02-08T05:40:05.277Z"
                },
                "bpp_details": {
                    "name": "ITC Store",
                    "symbol": "https://retailconnect.co.in/ONDC/itc-cart-1.png",
                    "short_desc": "Online eCommerce Store",
                    "long_desc": "Online eCommerce Store",
                    "images": [
                        "https://retailconnect.co.in/ONDC/itc-cart-1.png"
                    ],
                    "tags": [
                        {
                            "code": "bpp_terms",
                            "list": [
                                {
                                    "code": "np_type",
                                    "value": "ISN"
                                }
                            ]
                        }
                    ],
                    "bpp_id": "retailconnect.co.in"
                },
                "storeOpenTillDate": "2024-02-08T23:00:00.774Z"
            },
            {
                "id": "VVBWGLY+HONEY500",
                "time": {
                    "label": "enable",
                    "timestamp": "2024-02-08T05:40:05.277Z"
                },
                "descriptor": {
                    "name": "Vivel Body Wash, Glycerin & Honey, Moisturising Shower Gel, For Glowing skin, 500ml Pump, For women and men",
                    "code": "1:8905110004349",
                    "symbol": "http://admin.itcstore.in/media/catalog/product/s/k/sku_1801.png",
                    "short_desc": "Vivel Body Wash, Glycerin & Honey, Moisturising Shower Gel, For Glowing skin, 500ml Pump, For women and men",
                    "long_desc": "Vivel Body Wash, Glycerin & Honey, Moisturising Shower Gel, For Glowing skin, 500ml Pump, For women and men",
                    "images": [
                        "http://admin.itcstore.in/media/catalog/product/s/k/sku_1801.png",
                        "http://admin.itcstore.in/media/catalog/product/2/_/2_bd83803d-3bc4-40ed-9f5a-77c177e81ab2.jpg",
                        "http://admin.itcstore.in/media/catalog/product/3/_/3_09b70621-1f4c-4d0b-add5-2a9f4cdd951d.jpg"
                    ]
                },
                "quantity": {
                    "unitized": {
                        "measure": {
                            "unit": "gram",
                            "value": "500"
                        }
                    },
                    "available": {
                        "count": "99"
                    },
                    "maximum": {
                        "count": "5"
                    }
                },
                "price": {
                    "currency": "INR",
                    "value": "175.0",
                    "maximum_value": "240"
                },
                "category_id": "Beauty & Hygiene",
                "fulfillment_id": "1",
                "location_id": "ONDC-STORE-BGLR",
                "@ondc/org/returnable": true,
                "@ondc/org/cancellable": true,
                "@ondc/org/return_window": "P2D",
                "@ondc/org/seller_pickup_return": false,
                "@ondc/org/time_to_ship": "P1D",
                "@ondc/org/available_on_cod": false,
                "@ondc/org/contact_details_consumer_care": "Support Agent,support@itcstore.in,18003098994",
                "tags": [
                    {
                        "code": "origin",
                        "list": [
                            {
                                "code": "country",
                                "value": "IND"
                            }
                        ]
                    },
                    {
                        "code": "image",
                        "list": [
                            {
                                "code": "type",
                                "value": "back_image"
                            },
                            {
                                "code": "url",
                                "value": "http://admin.itcstore.in/media/catalog/product/s/k/sku_1801.png"
                            }
                        ]
                    },
                    {
                        "code": "veg_nonveg",
                        "list": [
                            {
                                "code": "veg",
                                "value": "yes"
                            }
                        ]
                    }
                ],
                "@ondc/org/statutory_reqs_prepackaged_food": {
                    "nutritional_info": "Yes",
                    "additives_info": "Yes",
                    "brand_owner_FSSAI_license_no": "11220303000336",
                    "other_FSSAI_license_no": "11220303000336",
                    "importer_FSSAI_license_no": "11220303000336",
                    "imported_product_country_of_origin": "IND"
                },
                "provider_details": {
                    "id": "ONDC-STORE-BGLR",
                    "descriptor": {
                        "name": "ITC Store",
                        "symbol": "https://retailconnect.co.in/ONDC/itc-cart-1.png",
                        "short_desc": "ITC Store",
                        "long_desc": "ITC Store",
                        "images": [
                            "https://retailconnect.co.in/ONDC/itc-cart-1.png"
                        ]
                    }
                },
                "location_details": {
                    "id": "ONDC-STORE-BGLR",
                    "gps": "12.8389239,77.6860114",
                    "address": {
                        "street": "Warehouse Building N, Khata No.2605/115and2606/114, Kammasandra Village, Anekal Taluk, Attibele Hobli",
                        "locality": "Kammasandra Village, Anekal Taluk, Attibele Hobli",
                        "city": "Bangalore",
                        "area_code": "560067",
                        "state": "KA"
                    },
                    "circle": {
                        "gps": "12.8389239,77.6860114",
                        "radius": {
                            "unit": "km",
                            "value": "50"
                        }
                    },
                    "time": {
                        "label": "enable",
                        "timestamp": "2024-02-08T05:40:05.277Z",
                        "days": "1,2,3,4,5,6,7",
                        "schedule": {
                            "holidays": []
                        },
                        "range": {
                            "start": "0700",
                            "end": "2300"
                        }
                    }
                },
                "category_details": {},
                "fulfillment_details": {
                    "id": "1",
                    "type": "Delivery"
                },
                "context": {
                    "domain": "nic2004:52110",
                    "country": "IND",
                    "city": "std:080",
                    "action": "on_search",
                    "core_version": "1.2.0",
                    "bap_id": "buyer-app-preprod.ondc.org",
                    "bap_uri": "https://buyer-app-preprod.ondc.org/protocol/v1",
                    "bpp_id": "retailconnect.co.in",
                    "bpp_uri": "https://retailconnect.co.in/ondc/public/OndcPreProd/callback",
                    "transaction_id": "c4e9650a-860e-47b0-b773-d3a5213ef52d",
                    "message_id": "858ebbc0-d54d-459e-ad04-5adc2a88ef21",
                    "timestamp": "2024-02-08T05:40:05.277Z"
                },
                "bpp_details": {
                    "name": "ITC Store",
                    "symbol": "https://retailconnect.co.in/ONDC/itc-cart-1.png",
                    "short_desc": "Online eCommerce Store",
                    "long_desc": "Online eCommerce Store",
                    "images": [
                        "https://retailconnect.co.in/ONDC/itc-cart-1.png"
                    ],
                    "tags": [
                        {
                            "code": "bpp_terms",
                            "list": [
                                {
                                    "code": "np_type",
                                    "value": "ISN"
                                }
                            ]
                        }
                    ],
                    "bpp_id": "retailconnect.co.in"
                },
                "storeOpenTillDate": "2024-02-08T23:00:00.775Z"
            },
            {
                "id": "8906009070902",
                "descriptor": {
                    "name": "UNIBIC Honey Oatmeal Cookies",
                    "Symbol": "https://m.media-amazon.com/images/I/413JbefebyL.jp",
                    "short_desc": "UNIBIC Honey Oatmeal Cookies",
                    "long_desc": "UNIBIC Honey Oatmeal Cookies",
                    "images": [
                        "https://m.media-amazon.com/images/I/413JbefebyL.jpg",
                        "https://uat.pep1.in/reg_barcode/upload/89060090709028405616957192705605664069425220056889.jpg",
                        "https://uat.pep1.in/reg_barcode/upload/89060090709023450716957192812401024684765929774378.jpg",
                        "https://uat.pep1.in/reg_barcode/NULL",
                        "https://uat.pep1.in/reg_barcode/NULL",
                        "https://uat.pep1.in/reg_barcode/upload/89060090709026947216957192902846104959041584271705.jpg"
                    ],
                    "code": "1:8906009070902"
                },
                "quantity": {
                    "available": {
                        "count": "20"
                    },
                    "maximum": {
                        "count": 3
                    }
                },
                "price": {
                    "currency": "INR",
                    "value": "30.0",
                    "maximum_value": "30"
                },
                "category_id": "Snacks and Namkeen",
                "fulfillment_id": "1",
                "location_id": "S01460808-BGLR",
                "@ondc/org/returnable": false,
                "@ondc/org/cancellable": false,
                "@ondc/org/return_window": "P2D",
                "@ondc/org/seller_pickup_return": false,
                "@ondc/org/time_to_ship": "PT1H",
                "@ondc/org/available_on_cod": false,
                "@ondc/org/contact_details_consumer_care": "Support Agent,support@quantumach.in,18003098994",
                "tags": {
                    "veg": "yes",
                    "non_veg": "no"
                },
                "@ondc/org/statutory_reqs_prepackaged_food": {
                    "nutritional_info": "Yes",
                    "additives_info": "Yes",
                    "brand_owner_FSSAI_license_no": "10821005001374",
                    "other_FSSAI_license_no": "10821005001374",
                    "importer_FSSAI_license_no": "10821005001374",
                    "imported_product_country_of_origin": "IND"
                },
                "provider_details": {
                    "id": "0e350d72-fa8f-4d84-a1cd-7fa721aa612d",
                    "descriptor": {
                        "name": "Pepsi Store - Shri Balaji Fruit And Vegetable",
                        "Symbol": "https://pep1.in/ondc_retail/nav-logo.png",
                        "short_desc": "Pepsi Store",
                        "long_desc": "Pepsi Store",
                        "images": [
                            "https://pep1.in/ondc_retail/nav-logo.png"
                        ]
                    }
                },
                "location_details": {
                    "id": "S01460808-BGLR",
                    "gps": "12.8389239,77.6860114",
                    "address": {
                        "street": "38CIL MAIN ROADBANGALORE BANGALORE BANGALORE KARNATAKA 560032",
                        "locality": "Bangalore",
                        "city": "Bangalore",
                        "area_code": "560067",
                        "state": "Karnataka"
                    },
                    "circle": {
                        "gps": "12.8389239,77.6860114",
                        "radius": {
                            "unit": "km",
                            "value": "3"
                        }
                    },
                    "time": {
                        "days": "1,2,3,4,5,6,7",
                        "schedule": {
                            "holidays": []
                        },
                        "range": {
                            "start": "0800",
                            "end": "2300"
                        }
                    }
                },
                "category_details": {},
                "fulfillment_details": {
                    "id": "1",
                    "type": "Delivery"
                },
                "context": {
                    "domain": "nic2004:52110",
                    "country": "IND",
                    "city": "std:080",
                    "action": "on_search",
                    "core_version": "1.1.0",
                    "bap_id": "buyer-app-preprod.ondc.org",
                    "bap_uri": "https://buyer-app-preprod.ondc.org/protocol/v1",
                    "bpp_id": "stage.pep1.in",
                    "bpp_uri": "https://stage.pep1.in/ondc/public/OndcPreProd/callback",
                    "transaction_id": "c4e9650a-860e-47b0-b773-d3a5213ef52d",
                    "message_id": "858ebbc0-d54d-459e-ad04-5adc2a88ef21",
                    "timestamp": "2024-02-08T05:40:05.611Z",
                    "ttl": "PT30S"
                },
                "bpp_details": {
                    "name": "Quantumach",
                    "symbol": "https://pep1.in/ondc_retail/nav-logo.png",
                    "short_desc": "Online eCommerce Store",
                    "long_desc": "Online eCommerce Store",
                    "images": [
                        "https://pep1.in/ondc_retail/nav-logo.png"
                    ],
                    "bpp_id": "stage.pep1.in"
                },
                "storeOpenTillDate": "2024-02-08T23:00:00.776Z"
            },
            {
                "id": "8906009070902",
                "descriptor": {
                    "name": "UNIBIC Honey Oatmeal Cookies",
                    "Symbol": "https://m.media-amazon.com/images/I/413JbefebyL.jp",
                    "short_desc": "UNIBIC Honey Oatmeal Cookies",
                    "long_desc": "UNIBIC Honey Oatmeal Cookies",
                    "images": [
                        "https://m.media-amazon.com/images/I/413JbefebyL.jpg",
                        "https://uat.pep1.in/reg_barcode/upload/89060090709028405616957192705605664069425220056889.jpg",
                        "https://uat.pep1.in/reg_barcode/upload/89060090709023450716957192812401024684765929774378.jpg",
                        "https://uat.pep1.in/reg_barcode/NULL",
                        "https://uat.pep1.in/reg_barcode/NULL",
                        "https://uat.pep1.in/reg_barcode/upload/89060090709026947216957192902846104959041584271705.jpg"
                    ],
                    "code": "1:8906009070902"
                },
                "quantity": {
                    "available": {
                        "count": "20"
                    },
                    "maximum": {
                        "count": 3
                    }
                },
                "price": {
                    "currency": "INR",
                    "value": "30.0",
                    "maximum_value": "30"
                },
                "category_id": "Snacks and Namkeen",
                "fulfillment_id": "1",
                "location_id": "S01433844-BGLR",
                "@ondc/org/returnable": false,
                "@ondc/org/cancellable": false,
                "@ondc/org/return_window": "P2D",
                "@ondc/org/seller_pickup_return": false,
                "@ondc/org/time_to_ship": "PT1H",
                "@ondc/org/available_on_cod": false,
                "@ondc/org/contact_details_consumer_care": "Support Agent,support@quantumach.in,18003098994",
                "tags": {
                    "veg": "yes",
                    "non_veg": "no"
                },
                "@ondc/org/statutory_reqs_prepackaged_food": {
                    "nutritional_info": "Yes",
                    "additives_info": "Yes",
                    "brand_owner_FSSAI_license_no": "10821005001374",
                    "other_FSSAI_license_no": "10821005001374",
                    "importer_FSSAI_license_no": "10821005001374",
                    "imported_product_country_of_origin": "IND"
                },
                "provider_details": {
                    "id": "8cdf6c74-8b95-4da1-9caa-3a0a5edd2508",
                    "descriptor": {
                        "name": "Pepsi Store - SMART NEEDS",
                        "Symbol": "https://pep1.in/ondc_retail/nav-logo.png",
                        "short_desc": "Pepsi Store",
                        "long_desc": "Pepsi Store",
                        "images": [
                            "https://pep1.in/ondc_retail/nav-logo.png"
                        ]
                    }
                },
                "location_details": {
                    "id": "S01433844-BGLR",
                    "gps": "28.4025,77.0886",
                    "address": {
                        "street": "Kammasandra Village, Anekal Taluk, Attibele Hobli",
                        "locality": "Kammasandra Village, Anekal Taluk, Attibele Hobli",
                        "city": "Bangalore",
                        "area_code": "560100",
                        "state": "Karnataka"
                    },
                    "circle": {
                        "gps": "28.4025,77.0886",
                        "radius": {
                            "unit": "km",
                            "value": "3"
                        }
                    },
                    "time": {
                        "days": "1,2,3,4,5,6,7",
                        "schedule": {
                            "holidays": []
                        },
                        "range": {
                            "start": "0800",
                            "end": "2300"
                        }
                    }
                },
                "category_details": {},
                "fulfillment_details": {
                    "id": "1",
                    "type": "Delivery"
                },
                "context": {
                    "domain": "nic2004:52110",
                    "country": "IND",
                    "city": "std:080",
                    "action": "on_search",
                    "core_version": "1.1.0",
                    "bap_id": "buyer-app-preprod.ondc.org",
                    "bap_uri": "https://buyer-app-preprod.ondc.org/protocol/v1",
                    "bpp_id": "stage.pep1.in",
                    "bpp_uri": "https://stage.pep1.in/ondc/public/OndcPreProd/callback",
                    "transaction_id": "c4e9650a-860e-47b0-b773-d3a5213ef52d",
                    "message_id": "858ebbc0-d54d-459e-ad04-5adc2a88ef21",
                    "timestamp": "2024-02-08T05:40:05.611Z",
                    "ttl": "PT30S"
                },
                "bpp_details": {
                    "name": "Quantumach",
                    "symbol": "https://pep1.in/ondc_retail/nav-logo.png",
                    "short_desc": "Online eCommerce Store",
                    "long_desc": "Online eCommerce Store",
                    "images": [
                        "https://pep1.in/ondc_retail/nav-logo.png"
                    ],
                    "bpp_id": "stage.pep1.in"
                },
                "storeOpenTillDate": "2024-02-08T23:00:00.776Z"
            },
            {
                "id": "fe3467e7-2104-46f3-9acf-10a65b0ad75d",
                "parent_item_id": "12121213232323",
                "time": {
                    "label": "enable",
                    "timestamp": "2024-02-07T13:30:20.979Z"
                },
                "descriptor": {
                    "name": "Corn Flakes",
                    "short_desc": "Corn Flakes",
                    "long_desc": "Corn Flakes Premium",
                    "symbol": "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png",
                    "images": [
                        "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png"
                    ]
                },
                "price": {
                    "currency": "INR",
                    "value": "899.0",
                    "maximum_value": "1099.0"
                },
                "quantity": {
                    "unitized": {
                        "measure": {
                            "unit": "gram",
                            "value": "500"
                        }
                    },
                    "available": {
                        "count": "99"
                    },
                    "maximum": {
                        "count": "99"
                    }
                },
                "@ondc/org/time_to_ship": "P2D",
                "location_id": "f13873c1-810d-4f2b-ba54-5edcec9f0e4a",
                "@ondc/org/returnable": true,
                "@ondc/org/return_window": "P7D",
                "@ondc/org/cancellable": true,
                "@ondc/org/seller_pickup_return": false,
                "@ondc/org/available_on_cod": false,
                "@ondc/org/contact_details_consumer_care": "Mayur Popli,mayur.popli@thewitslab.com,9876543210",
                "category_id": "Cereals and Breakfast",
                "@ondc/org/statutory_reqs_prepackaged_food": {
                    "manufacturer_or_packer_name": "Reebok Ind Pvt ltd.",
                    "manufacturer_or_packer_address": "Reebok India.\nVillage Kharar, P.O. Mohali, Dist. -Mohali (P.B.) -140301",
                    "common_or_generic_name_of_commodity": "Fashion",
                    "month_year_of_manufacture_packing_import": "January , 2023",
                    "nutritional_info": "Refer back image",
                    "additives_info": "Refer back image",
                    "brand_owner_FSSAI_license_no": "Refer back image",
                    "other_FSSAI_license_no": "Refer back image",
                    "importer_FSSAI_license_no": "12345678901234"
                },
                "tags": [
                    {
                        "code": "veg_nonveg",
                        "list": [
                            {
                                "code": "veg",
                                "value": "yes"
                            }
                        ]
                    },
                    {
                        "code": "origin",
                        "list": [
                            {
                                "code": "country",
                                "value": "IND"
                            }
                        ]
                    }
                ],
                "fulfillment_id": "c461a827-f43d-487e-871d-e13467acd866",
                "provider_details": {
                    "id": "ondc-mock-server-dev.thewitslab.com",
                    "descriptor": {
                        "name": "WITS ONDC TEST STORE",
                        "short_desc": "Wits Testing Store",
                        "long_desc": "Wits Testing Store",
                        "symbol": "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png",
                        "images": [
                            "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png"
                        ]
                    }
                },
                "location_details": {
                    "id": "f13873c1-810d-4f2b-ba54-5edcec9f0e4a",
                    "gps": "28.553440, 77.214241",
                    "address": {
                        "street": "7/6, August Kranti Marg",
                        "locality": "Siri Fort Institutional Area, Siri Fort",
                        "city": "New Delhi",
                        "state": "Delhi",
                        "area_code": "110049"
                    },
                    "circle": {
                        "gps": "28.553440, 77.214241",
                        "radius": {
                            "unit": "km",
                            "value": "10"
                        }
                    },
                    "time": {
                        "label": "enable",
                        "timestamp": "2024-02-07T13:30:20.979Z",
                        "days": "1,2,3,4,5,6,7",
                        "schedule": {
                            "holidays": []
                        },
                        "range": {
                            "start": "0000",
                            "end": "2359"
                        }
                    }
                },
                "category_details": {},
                "fulfillment_details": {
                    "id": "c461a827-f43d-487e-871d-e13467acd866",
                    "type": "Delivery"
                },
                "context": {
                    "domain": "nic2004:52110",
                    "country": "IND",
                    "city": "std:011",
                    "action": "on_search",
                    "core_version": "1.1.0",
                    "bap_id": "buyer-app-preprod.ondc.org",
                    "bap_uri": "https://buyer-app-preprod.ondc.org/protocol/v1",
                    "transaction_id": "c4e9650a-860e-47b0-b773-d3a5213ef52d",
                    "message_id": "858ebbc0-d54d-459e-ad04-5adc2a88ef21",
                    "timestamp": "2024-02-08T05:40:05.695Z",
                    "ttl": "PT30S",
                    "bpp_uri": "https://ondc-mock-server-dev.thewitslab.com/seller",
                    "bpp_id": "ondc-mock-server-dev.thewitslab.com"
                },
                "bpp_details": {
                    "name": "WITS ONDC TEST STORE",
                    "short_desc": "Wits Testing Store",
                    "long_desc": "Wits Testing Store",
                    "symbol": "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png",
                    "images": [
                        "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png"
                    ],
                    "bpp_id": "ondc-mock-server-dev.thewitslab.com"
                },
                "storeOpenTillDate": "2024-02-08T23:59:00.777Z"
            },
            {
                "id": "903b94ab-7605-4dd4-b0ff-d9ac92d3dd0e",
                "parent_item_id": "12121213232323",
                "time": {
                    "label": "enable",
                    "timestamp": "2024-02-07T13:30:20.979Z"
                },
                "descriptor": {
                    "name": "Honey",
                    "short_desc": "Honey , 300gm",
                    "long_desc": "Natural Honey Organic , 300gm",
                    "symbol": "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png",
                    "images": [
                        "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png"
                    ]
                },
                "price": {
                    "currency": "INR",
                    "value": "299.0",
                    "maximum_value": "309.0"
                },
                "quantity": {
                    "unitized": {
                        "measure": {
                            "unit": "gram",
                            "value": "300"
                        }
                    },
                    "available": {
                        "count": "0"
                    },
                    "maximum": {
                        "count": "0"
                    }
                },
                "@ondc/org/time_to_ship": "P2D",
                "location_id": "f13873c1-810d-4f2b-ba54-5edcec9f0e4a",
                "@ondc/org/returnable": true,
                "@ondc/org/return_window": "P7D",
                "@ondc/org/cancellable": true,
                "@ondc/org/seller_pickup_return": false,
                "@ondc/org/available_on_cod": false,
                "@ondc/org/contact_details_consumer_care": "Mayur Popli,mayur.popli@thewitslab.com,9876543210",
                "category_id": "Cereals and Breakfast",
                "@ondc/org/statutory_reqs_prepackaged_food": {
                    "manufacturer_or_packer_name": "Natural Ind Pvt ltd.",
                    "manufacturer_or_packer_address": "Natural India.\nVillage Kharar, P.O. Mohali, Dist. -Mohali (P.B.) -140301",
                    "common_or_generic_name_of_commodity": "Food and Beverages",
                    "month_year_of_manufacture_packing_import": "January , 2023",
                    "nutritional_info": "Refer back image",
                    "additives_info": "Refer back image",
                    "brand_owner_FSSAI_license_no": "Refer back image",
                    "other_FSSAI_license_no": "Refer back image",
                    "importer_FSSAI_license_no": "12345678901234"
                },
                "tags": [
                    {
                        "code": "veg_nonveg",
                        "list": [
                            {
                                "code": "veg",
                                "value": "yes"
                            }
                        ]
                    },
                    {
                        "code": "origin",
                        "list": [
                            {
                                "code": "country",
                                "value": "IND"
                            }
                        ]
                    }
                ],
                "fulfillment_id": "56d0f31d-20c9-4fe2-86c2-a6091af81df9",
                "provider_details": {
                    "id": "ondc-mock-server-dev.thewitslab.com",
                    "descriptor": {
                        "name": "WITS ONDC TEST STORE",
                        "short_desc": "Wits Testing Store",
                        "long_desc": "Wits Testing Store",
                        "symbol": "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png",
                        "images": [
                            "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png"
                        ]
                    }
                },
                "location_details": {
                    "id": "f13873c1-810d-4f2b-ba54-5edcec9f0e4a",
                    "gps": "28.553440, 77.214241",
                    "address": {
                        "street": "7/6, August Kranti Marg",
                        "locality": "Siri Fort Institutional Area, Siri Fort",
                        "city": "New Delhi",
                        "state": "Delhi",
                        "area_code": "110049"
                    },
                    "circle": {
                        "gps": "28.553440, 77.214241",
                        "radius": {
                            "unit": "km",
                            "value": "10"
                        }
                    },
                    "time": {
                        "label": "enable",
                        "timestamp": "2024-02-07T13:30:20.979Z",
                        "days": "1,2,3,4,5,6,7",
                        "schedule": {
                            "holidays": []
                        },
                        "range": {
                            "start": "0000",
                            "end": "2359"
                        }
                    }
                },
                "category_details": {},
                "fulfillment_details": {
                    "id": "56d0f31d-20c9-4fe2-86c2-a6091af81df9",
                    "type": "Self-Pickup"
                },
                "context": {
                    "domain": "nic2004:52110",
                    "country": "IND",
                    "city": "std:011",
                    "action": "on_search",
                    "core_version": "1.1.0",
                    "bap_id": "buyer-app-preprod.ondc.org",
                    "bap_uri": "https://buyer-app-preprod.ondc.org/protocol/v1",
                    "transaction_id": "c4e9650a-860e-47b0-b773-d3a5213ef52d",
                    "message_id": "858ebbc0-d54d-459e-ad04-5adc2a88ef21",
                    "timestamp": "2024-02-08T05:40:05.695Z",
                    "ttl": "PT30S",
                    "bpp_uri": "https://ondc-mock-server-dev.thewitslab.com/seller",
                    "bpp_id": "ondc-mock-server-dev.thewitslab.com"
                },
                "bpp_details": {
                    "name": "WITS ONDC TEST STORE",
                    "short_desc": "Wits Testing Store",
                    "long_desc": "Wits Testing Store",
                    "symbol": "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png",
                    "images": [
                        "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png"
                    ],
                    "bpp_id": "ondc-mock-server-dev.thewitslab.com"
                },
                "storeOpenTillDate": "2024-02-08T23:59:00.777Z"
            },
            {
                "id": "a34b412a-b2e4-4395-a175-a9f6ea388b4f",
                "parent_item_id": "12121213232323",
                "time": {
                    "label": "enable",
                    "timestamp": "2024-02-07T13:30:20.979Z"
                },
                "descriptor": {
                    "name": "Coffee Beans",
                    "short_desc": "Organic coffee , 100gm",
                    "long_desc": "Organic Premium Aromatic Coffee , 100gm",
                    "symbol": "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png",
                    "images": [
                        "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png"
                    ]
                },
                "price": {
                    "currency": "INR",
                    "value": "199.0",
                    "maximum_value": "209.0"
                },
                "quantity": {
                    "unitized": {
                        "measure": {
                            "unit": "gram",
                            "value": "100"
                        }
                    },
                    "available": {
                        "count": "99"
                    },
                    "maximum": {
                        "count": "99"
                    }
                },
                "@ondc/org/time_to_ship": "P2D",
                "location_id": "f13873c1-810d-4f2b-ba54-5edcec9f0e4a",
                "@ondc/org/returnable": true,
                "@ondc/org/return_window": "P7D",
                "@ondc/org/cancellable": false,
                "@ondc/org/seller_pickup_return": false,
                "@ondc/org/available_on_cod": false,
                "@ondc/org/contact_details_consumer_care": "Mayur Popli,mayur.popli@thewitslab.com,9876543210",
                "category_id": "Cereals and Breakfast",
                "category_ids": [
                    "L5qF1Aa5ENHK:1"
                ],
                "@ondc/org/statutory_reqs_prepackaged_food": {
                    "manufacturer_or_packer_name": "Natural Ind Pvt ltd.",
                    "manufacturer_or_packer_address": "Natural India.\nVillage Kharar, P.O. Mohali, Dist. -Mohali (P.B.) -140301",
                    "common_or_generic_name_of_commodity": "Food and Beverages",
                    "month_year_of_manufacture_packing_import": "January , 2023",
                    "nutritional_info": "Refer back image",
                    "additives_info": "Refer back image",
                    "brand_owner_FSSAI_license_no": "Refer back image",
                    "other_FSSAI_license_no": "Refer back image",
                    "importer_FSSAI_license_no": "12345678901234"
                },
                "tags": [
                    {
                        "code": "veg_nonveg",
                        "list": [
                            {
                                "code": "veg",
                                "value": "yes"
                            }
                        ]
                    },
                    {
                        "code": "origin",
                        "list": [
                            {
                                "code": "country",
                                "value": "IND"
                            }
                        ]
                    }
                ],
                "fulfillment_id": "a2afcb16-8d8d-47a9-b10a-12677f312dfa",
                "provider_details": {
                    "id": "ondc-mock-server-dev.thewitslab.com",
                    "descriptor": {
                        "name": "WITS ONDC TEST STORE",
                        "short_desc": "Wits Testing Store",
                        "long_desc": "Wits Testing Store",
                        "symbol": "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png",
                        "images": [
                            "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png"
                        ]
                    }
                },
                "location_details": {
                    "id": "f13873c1-810d-4f2b-ba54-5edcec9f0e4a",
                    "gps": "28.553440, 77.214241",
                    "address": {
                        "street": "7/6, August Kranti Marg",
                        "locality": "Siri Fort Institutional Area, Siri Fort",
                        "city": "New Delhi",
                        "state": "Delhi",
                        "area_code": "110049"
                    },
                    "circle": {
                        "gps": "28.553440, 77.214241",
                        "radius": {
                            "unit": "km",
                            "value": "10"
                        }
                    },
                    "time": {
                        "label": "enable",
                        "timestamp": "2024-02-07T13:30:20.979Z",
                        "days": "1,2,3,4,5,6,7",
                        "schedule": {
                            "holidays": []
                        },
                        "range": {
                            "start": "0000",
                            "end": "2359"
                        }
                    }
                },
                "category_details": {},
                "fulfillment_details": {
                    "id": "a2afcb16-8d8d-47a9-b10a-12677f312dfa",
                    "type": "Delivery and Self-Pickup"
                },
                "context": {
                    "domain": "nic2004:52110",
                    "country": "IND",
                    "city": "std:011",
                    "action": "on_search",
                    "core_version": "1.1.0",
                    "bap_id": "buyer-app-preprod.ondc.org",
                    "bap_uri": "https://buyer-app-preprod.ondc.org/protocol/v1",
                    "transaction_id": "c4e9650a-860e-47b0-b773-d3a5213ef52d",
                    "message_id": "858ebbc0-d54d-459e-ad04-5adc2a88ef21",
                    "timestamp": "2024-02-08T05:40:05.695Z",
                    "ttl": "PT30S",
                    "bpp_uri": "https://ondc-mock-server-dev.thewitslab.com/seller",
                    "bpp_id": "ondc-mock-server-dev.thewitslab.com"
                },
                "bpp_details": {
                    "name": "WITS ONDC TEST STORE",
                    "short_desc": "Wits Testing Store",
                    "long_desc": "Wits Testing Store",
                    "symbol": "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png",
                    "images": [
                        "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png"
                    ],
                    "bpp_id": "ondc-mock-server-dev.thewitslab.com"
                },
                "storeOpenTillDate": "2024-02-08T23:59:00.777Z"
            },
            {
                "id": "6dad73f7-2e1d-46c2-b273-fe041faeadaf",
                "parent_item_id": "QOs1sHRuDVZK",
                "time": {
                    "label": "enable",
                    "timestamp": "2024-02-07T13:30:20.979Z"
                },
                "descriptor": {
                    "name": "Wheat",
                    "short_desc": "Wits QA Wheat",
                    "long_desc": "Wits QA Wheat newly launched",
                    "symbol": "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png",
                    "images": [
                        "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png"
                    ]
                },
                "price": {
                    "currency": "INR",
                    "value": "199.0",
                    "maximum_value": "259.0"
                },
                "quantity": {
                    "unitized": {
                        "measure": {
                            "unit": "kilogram",
                            "value": "1"
                        }
                    },
                    "available": {
                        "count": "99"
                    },
                    "maximum": {
                        "count": "99"
                    }
                },
                "@ondc/org/time_to_ship": "P1D",
                "location_id": "f13873c1-810d-4f2b-ba54-5edcec9f0e4a",
                "@ondc/org/returnable": true,
                "@ondc/org/return_window": "P2D",
                "@ondc/org/cancellable": false,
                "@ondc/org/seller_pickup_return": false,
                "@ondc/org/available_on_cod": true,
                "@ondc/org/contact_details_consumer_care": "Mayur Popli,mayur.popli@thewitslab.com,9876543210",
                "category_id": "Cereals and Breakfast",
                "category_ids": [
                    "L5qF1Aa5ENHK:2"
                ],
                "related": true,
                "recommended": true,
                "@ondc/org/statutory_reqs_prepackaged_food": {
                    "manufacturer_or_packer_name": "Wits Ind Pvt ltd.",
                    "manufacturer_or_packer_address": "Wits India. Village Kharar, P.O. Mohali, Dist. Mohali (P.B.) 140301",
                    "common_or_generic_name_of_commodity": "Foodgrains",
                    "month_year_of_manufacture_packing_import": "January , 2023",
                    "nutritional_info": "Refer Box",
                    "additives_info": "Refer Box",
                    "brand_owner_FSSAI_license_no": "Refer Box",
                    "other_FSSAI_license_no": "Not Available",
                    "importer_FSSAI_license_no": "12345678901234"
                },
                "tags": [
                    {
                        "code": "origin",
                        "list": [
                            {
                                "code": "country",
                                "value": "IND"
                            }
                        ]
                    },
                    {
                        "code": "veg_nonveg",
                        "list": [
                            {
                                "code": "veg",
                                "value": "yes"
                            }
                        ]
                    }
                ],
                "fulfillment_id": "c461a827-f43d-487e-871d-e13467acd866",
                "provider_details": {
                    "id": "ondc-mock-server-dev.thewitslab.com",
                    "descriptor": {
                        "name": "WITS ONDC TEST STORE",
                        "short_desc": "Wits Testing Store",
                        "long_desc": "Wits Testing Store",
                        "symbol": "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png",
                        "images": [
                            "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png"
                        ]
                    }
                },
                "location_details": {
                    "id": "f13873c1-810d-4f2b-ba54-5edcec9f0e4a",
                    "gps": "28.553440, 77.214241",
                    "address": {
                        "street": "7/6, August Kranti Marg",
                        "locality": "Siri Fort Institutional Area, Siri Fort",
                        "city": "New Delhi",
                        "state": "Delhi",
                        "area_code": "110049"
                    },
                    "circle": {
                        "gps": "28.553440, 77.214241",
                        "radius": {
                            "unit": "km",
                            "value": "10"
                        }
                    },
                    "time": {
                        "label": "enable",
                        "timestamp": "2024-02-07T13:30:20.979Z",
                        "days": "1,2,3,4,5,6,7",
                        "schedule": {
                            "holidays": []
                        },
                        "range": {
                            "start": "0000",
                            "end": "2359"
                        }
                    }
                },
                "category_details": {},
                "fulfillment_details": {
                    "id": "c461a827-f43d-487e-871d-e13467acd866",
                    "type": "Delivery"
                },
                "context": {
                    "domain": "nic2004:52110",
                    "country": "IND",
                    "city": "std:011",
                    "action": "on_search",
                    "core_version": "1.1.0",
                    "bap_id": "buyer-app-preprod.ondc.org",
                    "bap_uri": "https://buyer-app-preprod.ondc.org/protocol/v1",
                    "transaction_id": "c4e9650a-860e-47b0-b773-d3a5213ef52d",
                    "message_id": "858ebbc0-d54d-459e-ad04-5adc2a88ef21",
                    "timestamp": "2024-02-08T05:40:05.695Z",
                    "ttl": "PT30S",
                    "bpp_uri": "https://ondc-mock-server-dev.thewitslab.com/seller",
                    "bpp_id": "ondc-mock-server-dev.thewitslab.com"
                },
                "bpp_details": {
                    "name": "WITS ONDC TEST STORE",
                    "short_desc": "Wits Testing Store",
                    "long_desc": "Wits Testing Store",
                    "symbol": "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png",
                    "images": [
                        "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png"
                    ],
                    "bpp_id": "ondc-mock-server-dev.thewitslab.com"
                },
                "storeOpenTillDate": "2024-02-08T23:59:00.778Z"
            },
            {
                "id": "ad193e16-1afd-4db6-b3c7-c22783633de9",
                "parent_item_id": "QOs1sHRuDVZK",
                "time": {
                    "label": "enable",
                    "timestamp": "2024-02-07T13:30:20.979Z"
                },
                "descriptor": {
                    "name": "Wheat",
                    "short_desc": "Wits QA Wheat",
                    "long_desc": "Wits QA Wheat newly launched",
                    "symbol": "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png",
                    "images": [
                        "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png"
                    ]
                },
                "price": {
                    "currency": "INR",
                    "value": "249.0",
                    "maximum_value": "299.0"
                },
                "quantity": {
                    "unitized": {
                        "measure": {
                            "unit": "kilogram",
                            "value": "2"
                        }
                    },
                    "available": {
                        "count": "99"
                    },
                    "maximum": {
                        "count": "99"
                    }
                },
                "@ondc/org/time_to_ship": "P1D",
                "location_id": "f13873c1-810d-4f2b-ba54-5edcec9f0e4a",
                "@ondc/org/returnable": true,
                "@ondc/org/return_window": "P2D",
                "@ondc/org/cancellable": false,
                "@ondc/org/seller_pickup_return": false,
                "@ondc/org/available_on_cod": true,
                "@ondc/org/contact_details_consumer_care": "Mayur Popli,mayur.popli@thewitslab.com,9876543210",
                "category_id": "Cereals and Breakfast",
                "category_ids": [
                    "L5qF1Aa5ENHK:2"
                ],
                "related": true,
                "recommended": true,
                "@ondc/org/statutory_reqs_prepackaged_food": {
                    "manufacturer_or_packer_name": "Wits Ind Pvt ltd.",
                    "manufacturer_or_packer_address": "Wits India.\nVillage Kharar, P.O. Mohali, Dist. -Mohali (P.B.) -140301",
                    "common_or_generic_name_of_commodity": "Foodgrains",
                    "month_year_of_manufacture_packing_import": "January , 2023",
                    "nutritional_info": "Refer Box",
                    "additives_info": "Refer Box",
                    "brand_owner_FSSAI_license_no": "Refer Box",
                    "other_FSSAI_license_no": "Not Available",
                    "importer_FSSAI_license_no": "12345678901234"
                },
                "tags": [
                    {
                        "code": "origin",
                        "list": [
                            {
                                "code": "country",
                                "value": "IND"
                            }
                        ]
                    },
                    {
                        "code": "veg_nonveg",
                        "list": [
                            {
                                "code": "veg",
                                "value": "yes"
                            }
                        ]
                    }
                ],
                "fulfillment_id": "c461a827-f43d-487e-871d-e13467acd866",
                "provider_details": {
                    "id": "ondc-mock-server-dev.thewitslab.com",
                    "descriptor": {
                        "name": "WITS ONDC TEST STORE",
                        "short_desc": "Wits Testing Store",
                        "long_desc": "Wits Testing Store",
                        "symbol": "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png",
                        "images": [
                            "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png"
                        ]
                    }
                },
                "location_details": {
                    "id": "f13873c1-810d-4f2b-ba54-5edcec9f0e4a",
                    "gps": "28.553440, 77.214241",
                    "address": {
                        "street": "7/6, August Kranti Marg",
                        "locality": "Siri Fort Institutional Area, Siri Fort",
                        "city": "New Delhi",
                        "state": "Delhi",
                        "area_code": "110049"
                    },
                    "circle": {
                        "gps": "28.553440, 77.214241",
                        "radius": {
                            "unit": "km",
                            "value": "10"
                        }
                    },
                    "time": {
                        "label": "enable",
                        "timestamp": "2024-02-07T13:30:20.979Z",
                        "days": "1,2,3,4,5,6,7",
                        "schedule": {
                            "holidays": []
                        },
                        "range": {
                            "start": "0000",
                            "end": "2359"
                        }
                    }
                },
                "category_details": {},
                "fulfillment_details": {
                    "id": "c461a827-f43d-487e-871d-e13467acd866",
                    "type": "Delivery"
                },
                "context": {
                    "domain": "nic2004:52110",
                    "country": "IND",
                    "city": "std:011",
                    "action": "on_search",
                    "core_version": "1.1.0",
                    "bap_id": "buyer-app-preprod.ondc.org",
                    "bap_uri": "https://buyer-app-preprod.ondc.org/protocol/v1",
                    "transaction_id": "c4e9650a-860e-47b0-b773-d3a5213ef52d",
                    "message_id": "858ebbc0-d54d-459e-ad04-5adc2a88ef21",
                    "timestamp": "2024-02-08T05:40:05.695Z",
                    "ttl": "PT30S",
                    "bpp_uri": "https://ondc-mock-server-dev.thewitslab.com/seller",
                    "bpp_id": "ondc-mock-server-dev.thewitslab.com"
                },
                "bpp_details": {
                    "name": "WITS ONDC TEST STORE",
                    "short_desc": "Wits Testing Store",
                    "long_desc": "Wits Testing Store",
                    "symbol": "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png",
                    "images": [
                        "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png"
                    ],
                    "bpp_id": "ondc-mock-server-dev.thewitslab.com"
                },
                "storeOpenTillDate": "2024-02-08T23:59:00.780Z"
            },
            {
                "id": "2f5944dd-8441-4c4e-987a-d2a1e022239b",
                "parent_item_id": "QOs1sHRuDVZK",
                "time": {
                    "label": "enable",
                    "timestamp": "2024-02-07T13:30:20.979Z"
                },
                "descriptor": {
                    "name": "Wheat",
                    "short_desc": "Wits QA Wheat",
                    "long_desc": "Wits QA Wheat newly launched",
                    "symbol": "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png",
                    "images": [
                        "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png"
                    ]
                },
                "price": {
                    "currency": "INR",
                    "value": "499.0",
                    "maximum_value": "699.0"
                },
                "quantity": {
                    "unitized": {
                        "measure": {
                            "unit": "kilogram",
                            "value": "5"
                        }
                    },
                    "available": {
                        "count": "99"
                    },
                    "maximum": {
                        "count": "99"
                    }
                },
                "@ondc/org/time_to_ship": "P1D",
                "location_id": "f13873c1-810d-4f2b-ba54-5edcec9f0e4a",
                "@ondc/org/returnable": true,
                "@ondc/org/return_window": "P2D",
                "@ondc/org/cancellable": false,
                "@ondc/org/seller_pickup_return": false,
                "@ondc/org/available_on_cod": true,
                "@ondc/org/contact_details_consumer_care": "Mayur Popli,mayur.popli@thewitslab.com,9876543210",
                "category_id": "Cereals and Breakfast",
                "category_ids": [
                    "L5qF1Aa5ENHK:2"
                ],
                "related": true,
                "recommended": true,
                "@ondc/org/statutory_reqs_prepackaged_food": {
                    "manufacturer_or_packer_name": "Wits Ind Pvt ltd.",
                    "manufacturer_or_packer_address": "Wits India.\nVillage Kharar, P.O. Mohali, Dist. -Mohali (P.B.) -140301",
                    "common_or_generic_name_of_commodity": "Foodgrains",
                    "month_year_of_manufacture_packing_import": "January , 2023",
                    "nutritional_info": "Refer Box",
                    "additives_info": "Refer Box",
                    "brand_owner_FSSAI_license_no": "Refer Box",
                    "other_FSSAI_license_no": "Not Available",
                    "importer_FSSAI_license_no": "12345678901234"
                },
                "tags": [
                    {
                        "code": "origin",
                        "list": [
                            {
                                "code": "country",
                                "value": "IND"
                            }
                        ]
                    },
                    {
                        "code": "veg_nonveg",
                        "list": [
                            {
                                "code": "veg",
                                "value": "yes"
                            }
                        ]
                    }
                ],
                "fulfillment_id": "c461a827-f43d-487e-871d-e13467acd866",
                "provider_details": {
                    "id": "ondc-mock-server-dev.thewitslab.com",
                    "descriptor": {
                        "name": "WITS ONDC TEST STORE",
                        "short_desc": "Wits Testing Store",
                        "long_desc": "Wits Testing Store",
                        "symbol": "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png",
                        "images": [
                            "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png"
                        ]
                    }
                },
                "location_details": {
                    "id": "f13873c1-810d-4f2b-ba54-5edcec9f0e4a",
                    "gps": "28.553440, 77.214241",
                    "address": {
                        "street": "7/6, August Kranti Marg",
                        "locality": "Siri Fort Institutional Area, Siri Fort",
                        "city": "New Delhi",
                        "state": "Delhi",
                        "area_code": "110049"
                    },
                    "circle": {
                        "gps": "28.553440, 77.214241",
                        "radius": {
                            "unit": "km",
                            "value": "10"
                        }
                    },
                    "time": {
                        "label": "enable",
                        "timestamp": "2024-02-07T13:30:20.979Z",
                        "days": "1,2,3,4,5,6,7",
                        "schedule": {
                            "holidays": []
                        },
                        "range": {
                            "start": "0000",
                            "end": "2359"
                        }
                    }
                },
                "category_details": {},
                "fulfillment_details": {
                    "id": "c461a827-f43d-487e-871d-e13467acd866",
                    "type": "Delivery"
                },
                "context": {
                    "domain": "nic2004:52110",
                    "country": "IND",
                    "city": "std:011",
                    "action": "on_search",
                    "core_version": "1.1.0",
                    "bap_id": "buyer-app-preprod.ondc.org",
                    "bap_uri": "https://buyer-app-preprod.ondc.org/protocol/v1",
                    "transaction_id": "c4e9650a-860e-47b0-b773-d3a5213ef52d",
                    "message_id": "858ebbc0-d54d-459e-ad04-5adc2a88ef21",
                    "timestamp": "2024-02-08T05:40:05.695Z",
                    "ttl": "PT30S",
                    "bpp_uri": "https://ondc-mock-server-dev.thewitslab.com/seller",
                    "bpp_id": "ondc-mock-server-dev.thewitslab.com"
                },
                "bpp_details": {
                    "name": "WITS ONDC TEST STORE",
                    "short_desc": "Wits Testing Store",
                    "long_desc": "Wits Testing Store",
                    "symbol": "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png",
                    "images": [
                        "https://res.cloudinary.com/dxum9bu0r/image/upload/v1706624067/Frame_qvtmt7.png"
                    ],
                    "bpp_id": "ondc-mock-server-dev.thewitslab.com"
                },
                "storeOpenTillDate": "2024-02-08T23:59:00.781Z"
            }
        ],
        "count": 296
    }
}

def parse_json(json_data):

    # Convert boolean literals to uppercase
    json_data = json_data.replace("true", "True").replace("false", "False")
    # Parse JSON data
    parsed_json = json.loads(json_data)
    arr = parsed_json.message.catalogs
    # payal shaura add your logic here 

    # list.append(templbl)
    # Process each received item
    for item in arr:
        # Accessing fields from the item
        name = item.name
        short_desc = item.short_desc
        long_desc = item.long_desc
        image = item.image
        symbol = item.symbol
                
                # Example: Print the fields of each item
        print("Name:", name)
        print("Short Description:", short_desc)
        print("Long Description:", long_desc)
        print("Images:", image)
        print("Symbol:", symbol)
       
        # score = tp.top(name, long_desc, short_desc, image, symbol, labels)
        # item.score = score
        return json.dumps(json_data)
        
        

parse_json(json)