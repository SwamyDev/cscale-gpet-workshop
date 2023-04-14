import argparse
import logging
from pathlib import Path

import rioxarray

from cscale_gpet_workshop.cpu.gaussian_blurr import gauss_blur


def main():
    parser = argparse.ArgumentParser(description="Performs a low pass gaussian blurr filter on the input GeoTiff.")
    parser.add_argument('in_tif', type=Path, help="Path to GeoTiff to be blurred")
    parser.add_argument('out_tif', type=Path, help="Output path of resulting blurred GeoTiff")
    parser.add_argument('-k', '--kernel-size', type=int, help="Size of the Gauss-Kernel (default: 3)", default=3)
    parser.add_argument('-s', '--sigma', type=float, help="Sigma of the Gauss-Kernel (default: 1.0)", default=1.0)
    args = parser.parse_args()
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

    gauss_blur(rioxarray.open_rasterio(args.in_tif), args.kernel_size, args.sigma).rio.to_raster(args.out_tif,
                                                                                                 compress='ZSTD')


if __name__ == "__main__":
    main()
