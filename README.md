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
  .............                                                            [100%]

  ----------- coverage: platform linux, python 3.7.5-final-0 -----------
  Name                        Stmts   Miss  Cover
  -----------------------------------------------
  marketservice/__init__.py       0      0   100%
  marketservice/models.py        35      0   100%
  marketservice/seed.py           2      0   100%
  marketservice/services.py      57      0   100%
  -----------------------------------------------
  TOTAL                          94      0   100%

  13 passed in 0.13s
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
