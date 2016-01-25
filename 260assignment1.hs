perfectNumber :: Int -> Int -> Int 
perfectNumber original check
  | original <= 0 = 0
  | mod original check == 0 = perfectNumber original-1 check
  | otherwise = perfectNumber original-1 check
