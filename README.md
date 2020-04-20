# farmersmarket
A checkout system for farmer's market

## Installation

- Build image
  ```
  docker build -t farmersmarket .
  ```

- Run test cases
  ```
  docker run farmersmarket
  ```
  ```
  λ → docker run farmersmarket
  ................                                                         [100%]

  ----------- coverage: platform linux, python 3.7.5-final-0 -----------
  Name                        Stmts   Miss  Cover
  -----------------------------------------------
  cli/__init__.py                 0      0   100%
  cli/app.py                     19      0   100%
  cli/utils.py                   16      0   100%
  marketservice/__init__.py       0      0   100%
  marketservice/models.py        35      0   100%
  marketservice/seed.py           2      0   100%
  marketservice/services.py      57      0   100%
  seed_data/__init__.py           0      0   100%
  seed_data/seed.py               0      0   100%
  setup.py                        2      2     0%
  -----------------------------------------------
  TOTAL                         131      2    98%

  16 passed in 0.19s
  ```

- Run CLI
  ```
  docker run -it farmersmarket /bin/bash
  ```

  ```
  λ → docker run -it farmersmarket /bin/bash
  root@429cfc5f44c5:/farmersmarket# farmersmarket
  Enter product codes: CF1 CF1 CH1 MK1
  Item 		  Price
  ---- 		  -----
  CF1 		  11.23
  CF1 		  11.23
     BOGO 	 -11.23
  CH1 		  3.11
  MK1 		  4.75
     CHMK 	 -4.75
  ------------------------
  Total: 		  14.34
  root@429cfc5f44c5:/farmersmarket#
  ```

## Assumption

As it's not clear from the problem statement, It is assumed that one
coupon/promo can be only applied on one item. So the order is important for 
conflicting coupons/promos.
