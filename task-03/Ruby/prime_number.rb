print "Enter a number:"
num = gets.chomp.to_i
if num < 2
  puts "No Prime"
else
  for i in 2..num
    count = 0
    for j in 2..i-1
      if i%j == 0
        count= 1
        break
      else
        count= 0
      end
    end
    if (count== 0)
      puts "#{i} \t"
    end
  end
end

