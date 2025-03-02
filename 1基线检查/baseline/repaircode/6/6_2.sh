#!/bin/bash

# 检查引导器类型
bootloader=$(grep -o 'GRUB|LILO' /etc/default/grub /etc/lilo.conf)

if [ "$bootloader" = "GRUB" ]; then

  # GRUB引导
  
  if [ -f "/boot/grub/menu.lst" ]; then
    # 配置密码
    sed -i 's/^password/password=password123/' /boot/grub/menu.lst
  else
    echo "WARNING: /boot/grub/menu.lst not found on GRUB system."
  fi

elif [ "$bootloader" = "LILO" ]; then

  # LILO引导

  if [ -f "/etc/lilo.conf" ]; then  
    # 配置密码
    sed -i 's/^password/password=password123/' /etc/lilo.conf
  else
    echo "WARNING: /etc/lilo.conf not found on LILO system."
  fi
  
else

  echo "Unknown bootloader, skip configuration."
  
fi

echo "Bootloader password set."
