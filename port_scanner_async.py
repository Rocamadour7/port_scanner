import asyncio
import time


async def check_port(ip, port):
    conn = asyncio.open_connection(ip, port)
    try:
        reader, writer = await asyncio.wait_for(conn, timeout=3)
    except:
        print('Port', port, 'is closed')
        return False
    else:
        print('Port', port, 'is open')
        return True
    finally:
        if 'writer' in locals():
            writer.close()


# Added because windows can't handle too many Selects.
async def check_port_semaphore(semaphore, ip, port):
    async with semaphore:
        return await check_port(ip, port)


if __name__ == '__main__':
    destinations = ['hackthissite.org']
    ports = range(1, 1025)

    print('#' * 50)
    print('Scanning {}'.format(' '.join(destinations)))
    print('#' * 50)

    tic = time.time()
    loop = asyncio.get_event_loop()

    gather = asyncio.gather(*[check_port(destination, port)
                              for destination in destinations for port in ports])

    # Use this if you are on Windows
    # semaphore = asyncio.Semaphore(500)  # This is because of Windows...ofc
    # gather = asyncio.gather(*[check_port_semaphore(semaphore, destination, port)
    #                           for destination in destinations for port in ports])
    loop.run_until_complete(gather)
    loop.close()

    print('#' * 50)
    toc = time.time()
    print('Total time: {:.2f} seconds'.format(toc - tic))
    # Total time: 3.17 seconds, local ip and hackthissite.org
    # Total time: 9.32 seconds, if on Windows
