import os, sys
from subprocess import call

import json
import urllib3
# curl -XGET 'http://localhost:9200/_nodes?os=true&process=true&pretty=true'

data = []
counter = 0

with open('data.json') as f:
    for line in f:
        # data.append(json.loads(line))
        data.append(line)
        try:
            call(['curl', '-XPUT', 'localhost:32769/catalogue/product/{}?pretty'.format(counter), '-d', line])
        except Exception as e:
            print("ERROR: " + str(e))
        finally:
            counter += 1
# test process
        if counter == 5:
            break

# Using the Bulk API
 POST /catalogue/product/_bulk --data-binary @data.json

curl -XPUT 'localhost:9200/markets?pretty' -d'
{
    "settings" : {
        "index" : {
            "number_of_shards" : 1,
            "number_of_replicas" : 1
        }
    }
}'

curl -XPUT 'localhost:9200/markets/product/1?pretty' -d'
{
    "aw_deep_link": "http://www.awin1.com/pclick.php?p=3600360137&a=78674&m=580",
    "product_name": "Koss Porta Pro On-Ear Headphones - White",
    "aw_product_id": "3600360137",
    "merchant_product_id": "cCH2805161212",
    "merchant_image_url": "http://www.picstop.co.uk/user/products/thumbnails/00164230abb.jpg",
    "description": "For those with refined musical taste, the lightweight Koss Porta Pro headphones are the most requested headphone on koss.com. These headphones are constructed from Mylar, which means the elements are extremely rigid, minimising mechanical distortion and ensuring exceedingly accurate sound reproduction. The Koss Porta Pro features dynamic elements that deliver exceptionally rich, deep bass, and a wide frequency response to capture every nuance in your favourite movie or musical performance. The headphones are built with a fully collapsible construction which is ideal for storage and transportation. The Comfort Zone setting on the temporal pad provides for a comfortable secure fit and the headphones come with an included convenient carrying case.  - The ultra portable on-ear headphones with dynamic element for extended frequency response - Comfort Zone setting on temporal pad for comfortable secure fit - The ultimate active headphones with a collapsible headband design for protective storage - Oxygen-free copper voice coils deliver deep bass and signal clarity - Includes a convenient carrying case for protective storage  Specifications Frequency Response: 15-25,000 Hz Impedance: 60 ohms Sensitivity: 101 dB SPL/1mW Cord: Straight, Dual Entry, 4ft",
    "merchant_category": "Audio > Headphones > On-Ear Headphones",
    "search_price": "27.99",
    "merchant_name": "PicStop",
    "merchant_id": "580",
    "category_name": "Headphones",
    "category_id": "22",
    "aw_image_url": "http://images.productserve.com/preview/0/580/37/01/3600360137.jpg",
    "currency": "GBP",
    "store_price": "",
    "delivery_cost": "",
    "merchant_deep_link": "http://www.picstop.co.uk/on-ear-headphones/koss-porta-pro-on-ear-headphones-white.html",
    "language": "en",
    "last_updated": "",
    "display_price": "GBP27.99",
    "data_feed_id": "10681",
    "Fashion:suitable_for": "",
    "Fashion:category": "",
    "Fashion:size": "",
    "Fashion:material": "",
    "Fashion:pattern": "",
    "Fashion:swatch": "",
    "brand_name": "Koss",
    "brand_id": "9066",
    "colour": "",
    "product_short_description": "",
    "specifications": "",
    "condition": "new",
    "product_model": "",
    "model_number": "",
    "dimensions": "",
    "keywords": "164230, 0164230, 00164230, Hama, Koss, Porta Pro portapro, On-Ear Headphones, headphones, wireless headphone, head phone, stereo, head phones, mp3 headphone, earphone, headset, head set, cheap headphone, mp3 headset, mp3 head set, onear, on ear, on-ear, earphones, ear phones,",
    "promotional_text": "Koss Porta Pro On-Ear Headphones - White are the ultimate active headphones with a collapsible headband for protective storage.  A Dynamic element for extended frequency response and Oxygen-free copper voice coils which give deep bass and signal clarity.",
    "product_type": "",
    "commission_group": "",
    "merchant_product_category_path": "",
    "merchant_product_second_category": "",
    "merchant_product_third_category": "",
    "rrp_price": "39.99",
    "saving": "",
    "savings_percent": "",
    "base_price": "",
    "base_price_amount": "",
    "base_price_text": "",
    "product_price_old": "",
    "delivery_restrictions": "",
    "delivery_weight": "",
    "warranty": "",
    "terms_of_contract": "",
    "delivery_time": "",
    "in_stock": "1",
    "stock_quantity": "",
    "valid_from": "",
    "valid_to": "",
    "is_for_sale": "1",
    "web_offer": "0",
    "pre_order": "0",
    "stock_status": "",
    "size_stock_status": "",
    "size_stock_amount": "",
    "merchant_thumb_url": "",
    "large_image": "http://www.picstop.co.uk/user/products/00164230abb.jpg",
    "alternate_image": "",
    "aw_thumb_url": "http://images.productserve.com/thumb/0/580/37/01/3600360137.jpg",
    "alternate_image_two": "",
    "alternate_image_three": "",
    "ean": "021299177297",
    "isbn": "",
    "upc": "",
    "mpn": "164230",
    "parent_product_id": "",
    "product_GTIN": "",
    "basket_link": ""
}'
