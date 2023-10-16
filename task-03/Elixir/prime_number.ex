defmodule PrimeNumbers do
  def main do
    IO.gets("Enter the limit: ") |> String.trim() |> String.to_integer() |> find_primes()
  end

  defp find_primes(n) when n < 2 do
    IO.puts("No Prime")
  end

  defp find_primes(n) do
    IO.write("The prime numbers are:")
    find_primes(2, n)
    IO.puts()
  end

  defp find_primes(n, n) do
    case is_prime(n, 2) do
      true -> IO.write(" #{n}")
      false -> :ok
    end
  end

  defp find_primes(i, n) do
    case is_prime(i, 2) do
      true -> IO.write(" #{i}")
      false -> :ok
    end
    find_primes(i + 1, n)
  end

  defp is_prime(2,2), do: true
  defp is_prime(n, 2) when rem(n,2) == 0, do: false
  defp is_prime(n, i) when i * i > n, do: true
  defp is_prime(n, i) when rem(n,i) == 0, do: false
  defp is_prime(n, i) do
    is_prime(n, i + 1)
  end
end

PrimeNumbers.main()
