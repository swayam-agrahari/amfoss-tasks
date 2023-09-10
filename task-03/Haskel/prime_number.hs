import Control.Monad

isPrime :: Integer -> Bool
isPrime n
    | n <= 1    = False
    | n <= 3    = True
    | otherwise = all (\x -> n `mod` x /= 0) [2..isqrt n]
    where isqrt = floor . sqrt . fromIntegral

main :: IO ()
main = do
    putStrLn "Enter the  limit:"
    input <- getLine
    let n = read input :: Integer
    putStrLn $ "Prime numbers are" ++ show n ++ ":"
    forM_ [2..n] $ \i -> when (isPrime i) (print i)
