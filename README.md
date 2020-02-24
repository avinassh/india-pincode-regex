# india-pincode-regex ![Packagist Version](https://img.shields.io/packagist/v/captn3m0/pincode?style=plastic) [![Build Status](https://travis-ci.org/captn3m0/india-pincode-regex.svg?branch=master)](https://travis-ci.org/captn3m0/india-pincode-regex)

Validate a [Postal Index Number][wiki] for India with a regex. The regexes are available in `regex.txt`. There are 2 regexes. The first validates PINs starting from 1-4, and the second validates the ones starting from 5-8. The reason for the split is to keep the regex size small. Currently they are both at 16K each.

## Source

The source for the data is the ["All India Pincode Directory"](https://data.gov.in/resources/all-india-pincode-directory) dataset on data.gov.in.

## Usage

The `regex.txt` file is 32KB in size, so you can easily use it wherever you want, including browsers.

### PHP

The package is available on [`packagist`](https://packagist.org/packages/captn3m0/pincode).

To use the PHP package:

```php
use PIN\Validator as P;
P::validate('110011'); // returns true;
```

## License

Licensed under the [MIT License](https://nemo.mit-license.org/). See LICENSE file for details.

[wiki]: https://en.wikipedia.org/wiki/Postal_Index_Number