from venv import logger


def get_valid_target_price() -> float:
    while True:
        try:
            user_input = input("Selecione o valor alvo para o Bitcoin (USD): ").strip()
            
            cleaned_input = user_input.replace(',', '.').replace(' ', '')
            
            if not cleaned_input:
                print("Erro: O campo não pode estar vazio. Tente novamente.")
                continue
            
            target_price = float(cleaned_input)
        
            if target_price <= 0:
                print("Erro: O valor deve ser maior que zero. Tente novamente.")
                continue
            
            if target_price < 1 or target_price > 10_000_000:
                print("Erro: Valor fora do intervalo válido ($1 - $10.000.000). Tente novamente.")
                continue

            confirm = input(f"\n✅ Confirmar valor alvo de ${target_price:,.2f}? (s/n): ").strip().lower()
            if confirm in ['s', 'sim', 'yes', 'y']:
                return target_price
            else:
                print("Operação cancelada. Vamos tentar novamente.\n")
                continue
                
        except ValueError:
            print("Erro: Digite apenas números (ex: 50000 ou 50000.50). Tente novamente.")
        except KeyboardInterrupt:
            print("\n\nOperação cancelada pelo usuário.")
            exit(0)
        except Exception as e:
            logger.error(f"Erro inesperado na validação: {e}")
            print("Erro inesperado. Tente novamente.")

